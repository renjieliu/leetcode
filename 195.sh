wc -l file.txt | awk '{if ($1 <10) print ""; else system("head -10 file.txt | tail -1"); }'