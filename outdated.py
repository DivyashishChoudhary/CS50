def main():
    month_key ={
        "January" :"01",
        "February" :"02",
        "March" :"03",
        "April" :"04",
        "May" :"05",
        "June" :"06",
        "July" :"07",
        "August" :"08",
        "September" :"09",
        "October" :"10",
        "November" :"11",
        "December" :"12"
    }
    while True:
            
        try:
            
            user_date = input("Date: ")
            if "/" in user_date:
                m,d,y = user_date.split("/")
                m,d,y = int(m), int(d), int(y)
                if m <=0 or m >12 or d <= 0 or d > 31 or y <= 0:
                    continue
                else:
                    print(f"{y}-{m:02d}-{d:02d}")
                    break
            else:
                md, y = user_date.split(",")
                y = int(y.strip())
                m,d = md.split(" ")
                m = m.strip()
                d = int(d.strip())
                if d <= 0 or d > 31 or y <= 0:
                    continue
                else:
                    print(f"{y}-{month_key[m]}-{d:02d}")
                    break
                


            

        except ValueError:

            continue

        except EOFError:
            print()
            break
        except KeyError:
            continue

main()
    