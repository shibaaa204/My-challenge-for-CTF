from pwn import *

p=process(["python3", "chall.py"])
p.sendline("""b'cAWa,=tDo9lp4!tc&=A/-.mkq38p_lMEWWA{e6v!2Rk:nL|N?;5d%`3F+{3,~Dk/ddEV+5qN"UUlv5a)W$R2pF9Rm|,tiD4-kA;s$V%^>]fi`(FX=q!!!!!&!!TQg(`eqew0"lddjjdd;;`vn"sdhccndjd000__--+;Hash Collision`'1$7ars_gdt"14241dw"sjsjs'__Q!@12/gf""".encode())
p.sendline("""b'cAWa,=tDo9lp4!tc&=A3-.mkq38p_lMEWWA{e6v!2Rk:nL|N?;5d%`3F+{3,~Dk/ddEV+5qN"UUlv5a)W$R2pF9Rm|,tiD4-kA;s$V%^>]fi`(FX=q!!!!!&!!TQg(`eqew0"lddjjdd;;`vn"sdhccndjd000__--+;Hash Collision`'1$7ars_gdt"14241dw"sjsjs'__Q!@12/gf""".encode())
p.interactive()
