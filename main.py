import site_list
import crawling_selenium

class main:
    
    def merge_arr(self):
        
        cs = crawling_selenium.crawling_selenium()
        sl = site_list.sl()
        sl_dict = sl.site_list
        magazine = sl_dict["bitcoinmagazine"]
        coindesk = sl_dict["coindesk"]
        cointelegraph = sl_dict["cointelegraph"]
        bloomingbit = sl_dict["bloomingbit"]
        
        title_arr1, href_arr1 = cs.crawling_with_selenium(magazine['url'], magazine['index'])
        title_arr2, href_arr2 = cs.crawling_with_selenium(coindesk['url'], coindesk['index'], sl.coindesk_xpath)
        title_arr3, href_arr3 = cs.crawling_with_selenium(cointelegraph['url'], cointelegraph['index'], sl.cointelegraph_xpath)
        title_arr4, href_arr4 = cs.crawling_with_selenium(bloomingbit['url'], bloomingbit['index'], sl.blommingbit_xpath)
        
        title_arr = title_arr1 + title_arr2 + title_arr3 + title_arr4
        href_arr = href_arr1 + href_arr2 + href_arr3 + href_arr4        
         
        return title_arr, href_arr
    
    def restructure_data(self):
        text =''
        title_arr, href_arr = self.merge_arr()
        num = len(title_arr)
        for i in num:
            result = title_arr[i] + '\n' + f'<a href={href_arr[i]}>링크</a>\n'
            text += result
            
        return text
                
# init = main()
# # title_data, href_data = init.merge_arr()
# init.restructure_data()

