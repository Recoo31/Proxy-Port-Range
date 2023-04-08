print(""" 
                                                (                    
                                                )\ )                 
                                                (()/(  (              
                                                /(_))))\ (  (    (   
                                                (_)) /((_))\ )\   )\  
                                                | _ (_)) ((_|(_) ((_) 
                                                |   / -_) _/ _ \/ _ \ 
                                                |_|_\___\__\___/\___/ 
                                                                    """)
print("                                                discord.gg/Xd8VfYPHB3")



def reco():
    with open('proxy.txt', 'r') as f: # 'proxy.txt' dosyasını okuyoruz
        ip_list = f.readlines() # Her bir IP adresini bir liste halinde alıyoruz

        start = int(input("1. Port: "))
        end = int(input("2. Port: "))+1

    with open('output.txt', 'w') as f: # 'output.txt' dosyasını yazmak için açıyoruz
        for ip in ip_list:
            ip = ip.strip() # Her bir IP adresini alıyoruz ve gereksiz boşlukları temizliyoruz
            for i in range(start, end+1):
                new_ip = ip + ":" + str(i) + "\n" # Her bir IP adresine numara ekliyoruz
                f.write(new_ip) # IP adresini 'output.txt' dosyasına yazıyoruz

reco()

