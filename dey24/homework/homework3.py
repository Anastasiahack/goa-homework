# წვეულებაზე მომსვლელი პიროვნებების სია :
names = [
    "Li Wei",       # ლი ვეი — ბიჭის სახელი, ნიშნავს "დიდებული"               ⬅ 0  -30
    "Wang Fang",    # ვანგ ფანგ — გოგოს სახელი, ნიშნავს "სურნელოვანი"           ⬅ 1  -29                                        
    "Zhang Wei",    # ჟანგ ვეი — ბიჭის სახელი, ნიშნავს "დიდებული"              ⬅  2  -28
    "Liu Yang",     # ლიუ იანგ — ბიჭის სახელი, ნიშნავს "ოკეანე"                 ⬅  3  -27
    "Chen Mei",     # ჩენ მეი — გოგოს სახელი, ნიშნავს "სილამაზე"                ⬅  4  -26
    "Zhao Jun",     # ჟაო ჯიუნ — ბიჭის სახელი, ნიშნავს "ჭკვიანი"                ⬅  5  -25
    "Sun Yue",      # სუნ იუე — გოგოს სახელი, ნიშნავს "მთვარე"  ✔️            ⬅  6  -24
    "Hu Tao",       # ჰუ ტაო — ბიჭის სახელი, ნიშნავს "ტალღა"                  ⬅  7  -23
    "Gao Ling",     # გაო ლინგ — გოგოს სახელი, ნიშნავს "ბრწყინვალება"          ⬅  8  -22
    "Lin Bo",       # ლინ ბო — ბიჭის სახელი, ნიშნავს "ფართო ცოდნა"           ⬅  9  -21
    "Xu Ai",        # სიუ აი — გოგოს სახელი, ნიშნავს "სიყვარული"              ⬅ 10  -20
    "He Zhi",       # ჰე ჟი — ბიჭის სახელი, ნიშნავს "მისწრაფება"  ✔️            ⬅11   -19 -10
    "Yang Hua",     # იანგ ჰუა — გოგოს სახელი, ნიშნავს "ყვავილი"               ⬅ 12  -18
    "Wu Liang",     # ვუ ლიანგ — ბიჭის სახელი, ნიშნავს "კეთილი"               ⬅ 13  -17
    "Ma Jing",      # მაე ჯინგ — გოგოს სახელი, ნიშნავს "სიმშვიდე"              ⬅ 14  -16                
    "Fang Tao",     # ფანგ ტაო — ბიჭის სახელი, ნიშნავს "ტალღა"   ✔️           ⬅ 15  -15  -13   
    "Deng Xiao",    # დენგ სიაო — გოგოს სახელი, ნიშნავს "განთიადი"  ✔️        ⬅ 16  -14  -13
    "Yin Lei",      # იინ ლეი — ბიჭის სახელი, ნიშნავს "მეხი" ✔️               ⬅ 17   -13  -13
    "Nie Ling",     # ნიე ლინგ — გოგოს სახელი, ნიშნავს "ელვარება" ✔️         ⬅ 18   -12  -13
    "Qin Jun",      # ჩინ ჯიუნ — ბიჭის სახელი, ნიშნავს "ელეგანტური"          ⬅ 19   -11
    "Zhou Min",     # ჟოუ მინ — გოგოს სახელი, ნიშნავს "ნათელი"               ⬅ 20   -10
    "Tang Rui",     # ტანგ რუი — გოგოს სახელი, ნიშნავს "სიბრძნე"              ⬅ 21  - 9
    "Xie Hao",      # სიე ჰაო — ბიჭის სახელი, ნიშნავს "შესანიშნავი"             ⬅ 22   -8
    "Luo Fei",      # ლუო ფეი — გოგოს სახელი, ნიშნავს "ფრენა"                ⬅ 23   -7 
    "Han Cheng",    # ჰან ჩენგ — ბიჭის სახელი, ნიშნავს "ქალაქი" ✔️              ⬅ 24   -6
    "Shi Yan",      # ში იენ — გოგოს სახელი, ნიშნავს "მშვენიერი"                ⬅ 25   -5
    "Jin Kai",      # ჯინ კაი — ბიჭის სახელი, ნიშნავს "გამხსნელი, წარმატებული" ⬅ 26   -4
    "Cai Lin",      # ცაი ლინ — გოგოს სახელი, ნიშნავს "ტყე"                    ⬅ 27   -3 
    "Bao Qiang",    # ბაო ჩიანგ — ბიჭის სახელი, ნიშნავს "ძვირფასი და ძლიერი"    ⬅ 28   -2
    "Meng Xue",     # მენგ სიუე — გოგოს სახელი, ნიშნავს "ოცნება და თოვლი"      ⬅ 29   -1
]

print(names)





Name_removed=names.pop(6)
print(Name_removed)
print(names)
  

Name_removed2=names.pop(10)
print(Name_removed2)
print(names)


Name_removed3=names.pop(13)
print(Name_removed3)
print(names)


Name_removed4=names.pop(13)
print(Name_removed4)
print(names)                                                                                        



Name_removed5=names.pop(13)
print(Name_removed5)
print(names)


Name_removed6=names.pop(13)
print(Name_removed6)
print(names)


Name_removed7=names.pop(18)
print(Name_removed7)
print(names)



print(len(names))

# ///////////////////////////////////////////////////////////////////////////////////////////////////////


names.append("Xu Jun" )
print(names)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////


names.insert(3,"Liu Wei")
print(names)


names.insert(4,"Wang Fang")
print(names)


names.insert(5,"Zhang Lei")
print(names)


names.insert(6,"Li Na")
print(names)


names.insert(7,"Chen Hao")
print(names)


names.insert(8,"Yang Mei")
print(names)


print(len(names))


First_list="თავდაპირველი სია არის 30"
print(First_list)


aAbbreviated_persons="ამოკლებული პიროვნებები : Sun Yue , He Zhi, Fang Tao, Deng Xiao , Yin Lei , Nie Ling , Han Cheng ,"
print(aAbbreviated_persons)


Added_persons="დამატებული პიროვნებები : Liu Wei, Wang Fang , Zhang Lei , Li Na , Chen Hao , Yang Mei, Xu Jun "
print(Added_persons)


Total="სულ დარჩა 30 პიროვნება"
print(Total)


Final_list="სიაში პიროვნებების რაოდენობა არის 30"
print(Final_list)

print(len(names))
      
