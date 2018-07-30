#!/usr/bin/python
#


import sys
import os
import ftplib
import ConfigParser
import urllib
import gzip
import csv


# Reading configuration file...
config = ConfigParser.ConfigParser()
config.read('JEKKO.cfg')

years = config.get('years', 'years').split(',')


numfrom = config.getint('nums','from')
numto = config.getint('nums','to')

wcfrom = config.getint('nums','wcfrom')
wcto = config.getint('nums','wcto')

threshold = config.getint('nums','threshold')





def concats(seq, start, stop):
    for mystr in seq:
        for num in xrange(start, stop):
            yield mystr + str(num)



def komb(seq, start):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + mystr1

if len(sys.argv) < 2 or sys.argv[1] == '-h':








        

        print " __  __         _      _    _         "
        print "|  \/  |_ __   | | ___| | _| | _____  "
        print "| |\/| | '__|  | |/ _ \ |/ / |/ / _ \ "
        print "| |  | | | | |_| |  __/   <|   < (_) |"
        print "|_|  |_|_|(_)___/ \___|_|\_\_|\_\___/ "



	print " Author : MR.JEKKO "
	print " Email    : JEKKOemail@gmail.com"
	print " Facebook : www.Facebook.com/GEEKINFO.A" 
	print " YouTube  : www.youtube.com/MRJEKKO "
	print "	[ Options ]\r\n"
	print "	-JEKKO bach tkhdam Script EX: JEKKO.py -JEKKO ! :)"

	exit()



elif sys.argv[1] == '-JEKKO':
	print "\r\n[+] Dkahkl Les Info Dyal Lvicitm bach Tsawb Lisr (dictionary)"
	print "[+] Ila ma3rftich chi haja gha brak 3la Enter ou Zid XD ! ;)\r\n"


# Chi info 3la Had Saaat =D  !

	name = raw_input("> smit had khouna: ").lower()
	while len(name) == 0 or name == " " or name == "  " or name == "   ":
		print "\r\n[-] Awayli Wach Ta Smya ma3rfhach -_- !"
		name = raw_input("> smit had khouna: ").lower()
	name = str(name)

	surname = raw_input("> Lknya Dyalou: ").lower()
	nick = raw_input("> La9ab Dyalou: ").lower()
	birthdate = raw_input("> Fo9ach Twald (DDMMYYYY): ")
	while len(birthdate) != 0 and len(birthdate) != 8:
		print "\r\n[-] Darouri Assat 8 Dr9ouma hna -_- ! "
		birthdate = raw_input("> Fo9ach Twald (DDMMYYYY): ")
	birthdate = str(birthdate)

	print "\r\n"

	wife = raw_input("> Smit Sahbou : ").lower()
	wifen = raw_input("> Lknya Dsahbou: ").lower()
	wifeb = raw_input("> F9oach Twald (DDMMYYYY): ")
	while len(wifeb) != 0 and len(wifeb) != 8:
		print "\r\n[-] Darouri Assat 8 Dr9ouma hna -_- !"
		wifeb = raw_input("> F9oach Twald (DDMMYYYY): ")
	wifeb = str(wifeb)
	print "\r\n"

	kid = raw_input("> 3ndou chi Brhouch Smitou : ").lower()
	kidn = raw_input("> Lknya Dyalou: ").lower()
	kidb = raw_input("> FO9ach Twlad  (DDMMYYYY): ")
	while len(kidb) != 0 and len(kidb) != 8:
		print "\r\n[-] Darouri Assat 6 Dr9ouma hna -_- !"
		kidb = raw_input("> FO9ach Twlad (DDMMYYYY): ")
	kidb = str(kidb)
	print "\r\n"

	pet = raw_input("> 3nddou chi Animal  smitou ?: ").lower()
	company = raw_input("> Smit charika dyalou : ").lower()
	print "\r\n"

	words = ['']
	words1 = raw_input("> Baghi Tzid chi m3loula haja 3la had khouna Y/[N]: ").lower()
	words2 = ""
	if words1 == "y":
		words2 = raw_input("> Dkhlhoum hna mtnsach Fasila, Bhal haka. [i.e. noob,3niba,khwaf], spaces madirhach: ").replace(" ","")
	words = words2.split(",")

	
	

	randnum = raw_input("> baghi tzid chi r9oma 3chwa3in Fkhar? Y/[N]").lower()
	leetmode = raw_input("> Wach Ndir Leet Mode  ? (i.e. leet = 1337) Y/[N]: ").lower()


	print "\r\n[+] Blati wahed Chwya ..."




	birthdate_yy = birthdate[-2:]
	birthdate_yyy = birthdate[-3:]
	birthdate_yyyy = birthdate[-4:]
	birthdate_xd = birthdate[1:2]
	birthdate_xm = birthdate[3:4]
	birthdate_dd = birthdate[:2]
	birthdate_mm = birthdate[2:4]

	wifeb_yy = wifeb[-2:]
	wifeb_yyy = wifeb[-3:]
	wifeb_yyyy = wifeb[-4:]
	wifeb_xd = wifeb[1:2]
	wifeb_xm = wifeb[3:4]
	wifeb_dd = wifeb[:2]
	wifeb_mm = wifeb[2:4]

	kidb_yy = kidb[-2:]
	kidb_yyy = kidb[-3:]
	kidb_yyyy = kidb[-4:]
	kidb_xd = kidb[1:2]
	kidb_xm = kidb[3:4]
	kidb_dd = kidb[:2]
	kidb_mm = kidb[2:4]
	
	
	
	nameup = name.title()
	surnameup = surname.title()
	nickup = nick.title()
	wifeup = wife.title()
	wifenup = wifen.title()
	kidup = kid.title()
	kidnup = kidn.title()
	petup = pet.title()
	companyup = company.title()
	wordsup = []
	for words1 in words:
		wordsup.append(words1.title())
	
	word = words+wordsup
	
	
	rev_name = name[::-1]
	rev_nameup = nameup[::-1]
	rev_nick = nick[::-1]
	rev_nickup = nickup[::-1]
	rev_wife = wife[::-1]
	rev_wifeup = wifeup[::-1]
	rev_kid = kid[::-1]
	rev_kidup = kidup[::-1]
	
	reverse = [rev_name, rev_nameup, rev_nick, rev_nickup, rev_wife, rev_wifeup, rev_kid, rev_kidup]
	rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
	rev_w = [rev_wife, rev_wifeup]
	rev_k = [rev_kid, rev_kidup]
	
	bds = [birthdate_yy, birthdate_yyy, birthdate_yyyy, birthdate_xd, birthdate_xm, birthdate_dd, birthdate_mm]
	
	bdss = []
	
	for bds1 in bds:
		bdss.append(bds1)
		for bds2 in bds:
			if bds.index(bds1) != bds.index(bds2):
				bdss.append(bds1+bds2)
				for bds3 in bds:
					if bds.index(bds1) != bds.index(bds2) and bds.index(bds2) != bds.index(bds3) and bds.index(bds1) != bds.index(bds3):
						bdss.append(bds1+bds2+bds3)
	
	
	
	wbds = [wifeb_yy, wifeb_yyy, wifeb_yyyy, wifeb_xd, wifeb_xm, wifeb_dd, wifeb_mm]
	
	wbdss = []
	
	for wbds1 in wbds:
		wbdss.append(wbds1)
		for wbds2 in wbds:
			if wbds.index(wbds1) != wbds.index(wbds2):
				wbdss.append(wbds1+wbds2)
				for wbds3 in wbds:
					if wbds.index(wbds1) != wbds.index(wbds2) and wbds.index(wbds2) != wbds.index(wbds3) and wbds.index(wbds1) != wbds.index(wbds3):
						wbdss.append(wbds1+wbds2+wbds3)
	
	
	
	kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm]
	
	kbdss = []
	
	for kbds1 in kbds:
		kbdss.append(kbds1)
		for kbds2 in kbds:
			if kbds.index(kbds1) != kbds.index(kbds2):
				kbdss.append(kbds1+kbds2)
				for kbds3 in kbds:
					if kbds.index(kbds1) != kbds.index(kbds2) and kbds.index(kbds2) != kbds.index(kbds3) and kbds.index(kbds1) != kbds.index(kbds3):
						kbdss.append(kbds1+kbds2+kbds3)
	
	
	kombinaac = [pet, petup, company, companyup]
	
	kombina = [name, surname, nick, nameup, surnameup, nickup]
	
	kombinaw = [wife, wifen, wifeup, wifenup, surname, surnameup]
	
	kombinak = [kid, kidn, kidup, kidnup, surname, surnameup]
	
	kombinaa = []
	for kombina1 in kombina:
		kombinaa.append(kombina1)
		for kombina2 in kombina:
			if kombina.index(kombina1) != kombina.index(kombina2) and kombina.index(kombina1.title()) != kombina.index(kombina2.title()):
				kombinaa.append(kombina1+kombina2)
	
	kombinaaw = []
	for kombina1 in kombinaw:
		kombinaaw.append(kombina1)
		for kombina2 in kombinaw:
			if kombinaw.index(kombina1) != kombinaw.index(kombina2) and kombinaw.index(kombina1.title()) != kombinaw.index(kombina2.title()):
				kombinaaw.append(kombina1+kombina2)
	
	kombinaak = []
	for kombina1 in kombinak:
		kombinaak.append(kombina1)
		for kombina2 in kombinak:
			if kombinak.index(kombina1) != kombinak.index(kombina2) and kombinak.index(kombina1.title()) != kombinak.index(kombina2.title()):
				kombinaak.append(kombina1+kombina2)
	
	
	
	komb1 = list(komb(kombinaa, bdss))
	komb2 = list(komb(kombinaaw, wbdss))
	komb3 = list(komb(kombinaak, kbdss))
	komb4 = list(komb(kombinaa, years))
	komb5 = list(komb(kombinaac, years))
	komb6 = list(komb(kombinaaw, years))
	komb7 = list(komb(kombinaak, years))
	komb8 = list(komb(word, bdss))
	komb9 = list(komb(word, wbdss))
	komb10 = list(komb(word, kbdss))
	komb11 = list(komb(word, years))
	komb12 = ['']
	komb13 = ['']
	komb14 = ['']
	komb15 = ['']
	komb16 = ['']
	komb21 = ['']
	if randnum == "y":
		komb12 = list(concats(word, numfrom, numto))
		komb13 = list(concats(kombinaa, numfrom, numto))
		komb14 = list(concats(kombinaac, numfrom, numto))
		komb15 = list(concats(kombinaaw, numfrom, numto))
		komb16 = list(concats(kombinaak, numfrom, numto))
		komb21 = list(concats(reverse, numfrom, numto))
	komb17 = list(komb(reverse, years))
	komb18 = list(komb(rev_w, wbdss))
	komb19 = list(komb(rev_k, kbdss))
	komb20 = list(komb(rev_n, bdss))
	komb001 = ['']
	komb002 = ['']
	komb003 = ['']
	komb004 = ['']
	komb005 = ['']
	komb006 = ['']
	
	
	print "[+] List katwjad ou kaytmsh dakchi lim3awd"
	
	komb_unique1 = dict.fromkeys(komb1).keys()
	komb_unique2 = dict.fromkeys(komb2).keys()
	komb_unique3 = dict.fromkeys(komb3).keys()
	komb_unique4 = dict.fromkeys(komb4).keys()
	komb_unique5 = dict.fromkeys(komb5).keys()
	komb_unique6 = dict.fromkeys(komb6).keys()
	komb_unique7 = dict.fromkeys(komb7).keys()
	komb_unique8 = dict.fromkeys(komb8).keys()
	komb_unique9 = dict.fromkeys(komb9).keys()
	komb_unique10 = dict.fromkeys(komb10).keys()
	komb_unique11 = dict.fromkeys(komb11).keys()
	komb_unique12 = dict.fromkeys(komb12).keys()
	komb_unique13 = dict.fromkeys(komb13).keys()
	komb_unique14 = dict.fromkeys(komb14).keys()
	komb_unique15 = dict.fromkeys(komb15).keys()
	komb_unique16 = dict.fromkeys(komb16).keys()
	komb_unique17 = dict.fromkeys(komb17).keys()
	komb_unique18 = dict.fromkeys(komb18).keys()
	komb_unique19 = dict.fromkeys(komb19).keys()
	komb_unique20 = dict.fromkeys(komb20).keys()
	komb_unique21 = dict.fromkeys(komb21).keys()
	komb_unique01 = dict.fromkeys(kombinaa).keys()
	komb_unique02 = dict.fromkeys(kombinaac).keys()
	komb_unique03 = dict.fromkeys(kombinaaw).keys()
	komb_unique04 = dict.fromkeys(kombinaak).keys()
	komb_unique05 = dict.fromkeys(word).keys()
	komb_unique07 = dict.fromkeys(komb001).keys()
	komb_unique08 = dict.fromkeys(komb002).keys()
	komb_unique09 = dict.fromkeys(komb003).keys()
	komb_unique010 = dict.fromkeys(komb004).keys()
	komb_unique011 = dict.fromkeys(komb005).keys()
	komb_unique012 = dict.fromkeys(komb006).keys()
	
	uniqlist = bdss+wbdss+kbdss+reverse+komb_unique01+komb_unique02+komb_unique03+komb_unique04+komb_unique05+komb_unique1+komb_unique2+komb_unique3+komb_unique4+komb_unique5+komb_unique6+komb_unique7+komb_unique8+komb_unique9+komb_unique10+komb_unique11+komb_unique12+komb_unique13+komb_unique14+komb_unique15+komb_unique16+komb_unique17+komb_unique18+komb_unique19+komb_unique20+komb_unique21+komb_unique07+komb_unique08+komb_unique09+komb_unique010+komb_unique011+komb_unique012
	
	unique_lista = dict.fromkeys(uniqlist).keys()
	unique_leet = []
	if leetmode == "y":
		for x in unique_lista: 
			x = x.replace('a',a)
			x = x.replace('i',i)
			x = x.replace('e',e)
			x = x.replace('t',t)
			x = x.replace('o',o)
			x = x.replace('s',s)
			x = x.replace('g',g)
			x = x.replace('z',z)
			unique_leet.append(x)
	
	unique_list = unique_lista + unique_leet
	
	unique_list_finished = []
	for x in unique_list:
		if len(x) > wcfrom and len(x) < wcto:
			unique_list_finished.append(x)

	unique_list_finished.sort()
	f = open ( name+'.txt', 'w' )
	f.write (os.linesep.join(unique_list_finished))
	f = open ( name+'.txt', 'r' )
	lines = 0
	for line in f:
		lines += 1
	f.close()
	
	print "[+] List kayn F Folder Dyal Script \033[1;31m"+name+".txt\033[1;m, counting \033[1;31m"+str(lines)+"\033[1;m words."


	exit()

	
	
