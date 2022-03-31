from datetime import datetime
import mysql.connector
import shutil

mydb = mysql.connector.connect(
    host="localhost",
    user="root",#root is the defult username for mysql
    #password of database that setted when you download mysql
    password="LionKing123$",
    #name of database that have created
    database="sistemparkir"
)
mycursor=mydb.cursor()

columns=shutil.get_terminal_size().columns
print("Selamat Datang ke sistem parkir saya".center(columns))

def main ():
    print("[A] Semak harga bagi setiap jenis kenderaan")
    print("[B] Membuat Parkir")
    print("[C] Membuat bayaran parkir")
    print("[D] Semak kenderaan yang sedang parkir")
    print("[E] Hentikan program ini")
    menu=input("Sila masukkan pilihan anda: ")
    if menu == "A":
        def semak():
            print("[1] Kenderaan motosikal dan basikal")
            print("[2] Kenderaan kereta")
            print("[3] Kenderaan besar")
            print("[4] Pulang ke menu")
            check=(input("Masukkan pilihan anda: "))
            if check =="1":
                print("Kepada Kad parkir ,masa parkir yang kurang atau sama dengan 2 jam,bayaran parkir=RM3")
                print("Selepas itu,bayaran parkir ialah RM1 sejam")
                print("Kepada penggunaan tiket,semua bayaran tambah RM1")
                main()
            elif check =="2":
                print("Kepada Kad parkir,masa parkir yang kurang atau sama dengan 2 jam,bayaran parkir=RM3")
                print("Selepas itu,bayaran parkir ialah RM2 sejam")
                print("Kepada penggunaan tiket,semua bayaran tambah RM1")
                main()
            elif check =="3":
                print("Kepada Kad parkir,masa parkir yang kurang atau sama dengan 2 jam,bayaran parkir=RM4")
                print("Selepas itu,bayaran parkir ialah RM3 sejam")
                print("Kepada penggunaan tiket,semua bayaran tambah RM1")
                main()
            elif check =="4":
                main()
            else:
                print("INVALID INPUT,SILA MASUK LAGI")
                semak()
        semak()
    elif menu == "B":
        def parkir():
            print("Sila masukkan jenis kenderaan")
            print("[1] Kenderaan motosikal dan basikal")
            print("[2] Kenderaan kereta")
            print("[3] Kenderaan besar")
            print("[4] Pulang ke menu")
            global jenis
            jenis=input("Masukkan pilihan anda: ")
            if jenis == "1":
                print("Kenderaan motosikal dan basikal")
                kenderaan=("Kenderaan motosikal dan basikal")
            elif jenis =="2":
                print("Kenderaan kereta")
                kenderaan=("Kenderaan kereta")
            elif jenis =="3":
                print("Kenderaan besar")
                kenderaan=("Kenderaan besar")
            elif jenis =="4":
                #loop back to main
                main()
            else:
                print("INVALID INPUT,SILA MASUK LAGI")
                print("Sila masuk lagi")
                parkir()
            global carplate
            carplate=input("Sila masukkan nomber carplate: ")
            my_string= str(input('\n Sila masukkan masa mula parkir(yyyy-mm-dd hh:mm): '))
            masa=datetime.now()
            sql = "INSERT INTO customers (nombor_carplate, jenis_kenderaan, masa_mula_parkir) VALUES (%s,%s,%s)"
            val = (carplate,kenderaan,my_string,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("rekod telah dimasuk")
            print("Inilah id parkir: ",mycursor.lastrowid)
            main()
        parkir()
    elif menu == "C":
        def bayar():
            id_masuk=input("Untuk menjalankan bayaran, sila masukkan id parkir: ")
            quary1=("SELECT * FROM customers WHERE id = %s")
            value1=(id_masuk,)
            mycursor.execute(quary1,value1)
            result1=mycursor.fetchall()
            for x in result1:
                print(x)
            choice=input("Adakah informasi adalah betul, Jika betul, tekan Y: ")
            if choice == "Y":
                masa=datetime.now()
                quary=("SELECT masa_mula_parkir FROM customers WHERE id = %s")
                value=(id_masuk,)
                mycursor.execute(quary,value)
                result=mycursor.fetchone()
                for x in result:
                    global my_date2
                    my_date2=x
                    print(my_date2)
                    my_date3=datetime.strptime(my_date2, "%Y-%m-%d %H:%M")
                time_delta = (masa-my_date3)
                total_seconds=time_delta.total_seconds()
                global hour
                hour=int(total_seconds/60/60)
                cara=input("Jika ada kad parkir, sila tekan Y: ")
                quary2=("SELECT jenis_kenderaan FROM customers WHERE id = %s")
                value2=(id_masuk,)
                mycursor.execute(quary2,value2)
                result2=mycursor.fetchone()
                for x in result2:
                    global jenis2
                    jenis2=x
                    print(jenis2)
                if jenis2 == "Kenderaan motosikal dan basikal":
                    if cara =="Y":
                        if hour<=2:
                            fee=int(3)
                        else:
                            fee=((hour-2)*int(1))
                    else:
                        if hour<=2:
                            fee=int(4)
                        else:
                            fee=((hour-2)*int(2))
                elif jenis2 =="Kenderaan kereta":
                    if cara =="Y":
                        if hour<=2:
                            fee=int(3)
                        else:
                            fee=((hour-2)*int(2))
                    else:
                        if hour<=2:
                            fee=int(4)
                        else:
                            fee=((hour-2)*int(3))
                elif jenis2 == "Kenderaan besar":
                    if cara =="Y":
                        if hour<=2:
                            fee=int(4)
                        else:
                            fee=((hour-2)*int(3))
                    else:
                        if hour<=2:
                            fee=int(5)
                        else:
                            fee=((hour-2)*int(4))
                print("\t Bayaran parkir ialah RM",round(fee,2))
                bayar=float(input("Sila masukkan bayaran parkir yang dapat: "))
                def change():
                    while bayar!=fee:
                        if bayar > fee:
                            print("Inilah change RM",round(bayar-fee,2))
                            print("TERIMA KASIH kerana datang".center(columns))
                            print("Sila datang lagi".center(columns))
                            delete="DELETE FROM customers WHERE id = %s"
                            delete2=(id_masuk,)
                            mycursor.execute(delete,delete2)
                            mydb.commit()
                            main()
                        else:
                            print("Bayaran yang diberi tidak cukup")
                            global bayaran_kurang
                            bayaran_kurang=(fee-bayar)
                            print("Inilah bayaran yang perlu dibayar lagi",round(bayaran_kurang,2))
                            def lebih ():
                                bayar_lagi=float(input("Sila masukkan bayaran lagi: "))
                                bayaran_lagi=(bayaran_kurang-bayar_lagi)
                                while bayaran_lagi!=0:
                                    lebih()
                                else:
                                    print("TERIMA KASIH".center(columns))
                                    delete="DELETE FROM customers WHERE id = %s"
                                    delete2=(id_masuk,)
                                    mycursor.execute(delete,delete2)
                                    mydb.commit()
                                    main()
                            lebih()
                    else:
                        print("TERIMA KASIH".center(columns))
                        delete="DELETE FROM customers WHERE id = %s"
                        delete2=(id_masuk,)
                        mycursor.execute(delete,delete2)
                        mydb.commit()
                        main()
                change()
            else:
                print("Sila masukkan id parkir lagi")
                main()
        bayar()
    elif menu == "D":
        def semak_kenderaan():
            cp_masuk=input("Untuk semak kenderaan,sila masukkan nombor carplate: ")
            quary2=("SELECT * FROM customers WHERE nombor_carplate = %s")
            value2=(carplate,)
            mycursor.execute(quary2,value2)
            result2= mycursor.fetchall()
            for y in result2:
                print(y)
            main()
        semak_kenderaan()
    elif menu == "E":
        def finish():
            print("Terima kasih kerana guna program ini")
            if mydb.is_connected:
                mycursor.close()
                mydb.close()
                print("Perhubungan MySQL telah dihenti")
        finish()
    else:
        print("INVALID INPUT")
        main()
main()