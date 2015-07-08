# -*- coding: utf-8 -*-
import scrapy
import json

from datoscba.items import GobItem


class MesasSpider(scrapy.Spider):
    name = "mesas"
    allowed_domains = ["eleccionescordoba.gob.ar"]
    start_urls = (
        'http://www.resultados.eleccionescordoba.gob.ar/r/0/Reg_04000000.html',
    )
    base = "http://www.resultados.eleccionescordoba.gob.ar/"
    #handle_httpstatus_list = [302, 404]


    def parse(self, resp):
        links = resp.css(".region-nav-item a").xpath("@href").extract()

        if "/lvg/" in resp.url:
            code = resp.url.split("/")[-2]
            code2 = resp.css("script").re("lvgCode = \w+")[0].replace("lvgCode = ", "")
            tally = "1" # 1 es gobernador
            url = "http://www.resultados.eleccionescordoba.gob.ar/tallies/%s/%s/%s.json" % (code, code2, tally)
            mesa = resp.css('meta[name="author"]').xpath("@content").extract()[0]

            yield scrapy.http.Request(url, self.parse_gob, meta={"mesa": mesa, "origin": resp.url})

        else:
            for link in links:
                if "/lvg/" not in resp.url:
                    yield self.make_requests_from_url(self.base + link.replace("../../", ""))

    def parse_gob(self, resp):
        jresp = json.loads(resp.body)
        gob = GobItem()
        gob["mesa"] = int(resp.meta["mesa"])
        total = 0
        for row in jresp["optionsRegister"]:
            gob[row["partyAbb"]] = row["amount"]
            total += row["amount"]
        gob["blancos"] = jresp["emptyVotesAmount"]
        gob["nulos"] = jresp["nullVotesAmount"]

        return [gob]
