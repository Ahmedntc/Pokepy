#how to run = "scrapy runspider main.py -o saida.csv"

import scrapy

class PokeSpider(scrapy.Spider):
  name = 'pokespider'
  start_urls = ['https://pokemondb.net/pokedex/all']

  def parse(self, response):

    ### tabela de seletores de CSS
    tabela_pokedex = "table#pokedex > tbody > tr"

    linhas = response.css(tabela_pokedex)
    for linha in linhas:
      coluna_href = linha.css("td:nth-child(2) > a::attr(href)")
  
    
      
      yield response.follow(coluna_href.get(), self.parser_pokemon)
          
      
  def parser_pokemon(self, response): 
    name_s  = "#main > h1::text"
    id_s ="div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(1) > td > strong::text"
    type_s = " div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(2) > td > a::text"
    height_selector = "div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(4) > td::text"
    weight_selector = "div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(5) > td::text"
    ability_selector ="div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(6) > td > * > a::attr(href)"
    evolve_selector = "#main > div.infocard-list-evo > * > span:nth-child(2) > a::text"
    name = response.css(name_s)
    type = response.css(type_s)
    height = response.css(height_selector)
    id = response.css(id_s)
    weight = response.css(weight_selector)
    ability_url = response.css(ability_selector).getall()
    evolution = response.css(evolve_selector).getall()
   # nomeH, descH = self.parse_habilidade(ability_url)
    Hab = []
    for i in range(len(ability_url)):
      Hab.append(ability_url[i].split("/"))
      
    nameHab = []
    for i in range(len(Hab)):
      nameHab.append(Hab[i][2])

    yield {'Id': id.get(), 'Nome': name.get(), 'Type': type.getall(), 'Altura': height.get(), 'Peso': weight.get(), "Urls das Habilidades": ability_url,"Nomes das Habilidades": nameHab,  "Evoluções": evolution}




 # def parse_habilidade(self, response):
 #   nomeHab = " #main > h1::text"
 #  descHab = " div.grid-row > div:nth-child(1) > p"
 #  nomeH = response.css(nomeHab).get()
 #  descH = response.css(descHab).get()
 #  return nomeH, descH
    
    
    