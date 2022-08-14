import time

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



port1 = int(input("1. Port: "))
port2 = int(input("2. Port: "))+1

class Recoo:
    def reco(self):
        with open("iplist.txt", 'r') as superim:
            x = len(superim.readlines())
            if x > 0:
                    i = open("iplist.txt", "r")
                    ipi = i.readline().rstrip('\n')
                    lines = i.readlines()
                    ip =ipi+':'
                    a = open("İp.txt","a")
                    for x in range(port1,port2):
                        reco=ip+str(x)+'\n'
                        a.write(reco)
                    with open("iplist.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != "%s" % (ipi,):
                                f.write(line)
                    a.close()
                    return self.reco()

            else:
                print("Iplist boş")
                print("Iplist boş")
                print("Iplist boş")
                print("Iplist boş")
                print("Iplist boş")
                time.sleep(1)
                exit()


Recoo().reco()

