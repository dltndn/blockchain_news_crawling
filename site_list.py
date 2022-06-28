class sl:
      
  site_list = {
    'bitcoinmagazine' : {"url" : 'https://bitcoinmagazine.com',
                        "index" : 0},
    'coindesk' : {"url" : 'https://www.coindesk.com',
                  "index" : 1},
    'cointelegraph' : {"url" : 'https://cointelegraph.com',
                      "index" : 2},
    'bloomingbit' : {"url" : 'https://bloomingbit.io/news/',
                    "index" : 3}
  }
  
  coindesk_xpath = '//*[@id="fusion-app"]/div/div[2]/div/main/div[2]/section[1]/div/div[2]/div/div[1]/div/div/div[2]'
  cointelegraph_xpath = '//*[@id="__layout"]/div/div[1]/main/div/div/div[2]/div/ul'
  blommingbit_xpath = '//*[@id="__layout"]/div/div[1]/div/section[2]/section[2]'