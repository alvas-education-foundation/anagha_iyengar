#i ncl ude<st di o. h>
#i ncl ude<st dl i b. h>
st r uctnode
{
i nti nf o;
st r uctnode* pt r ;
} * t op, * t op1, * t emp;
i ntt opel ement ( ) ;
v oi dpush( i ntdat a) ;
v oi dpop( ) ;
v oi dempt y ( ) ;
v oi ddi spl ay ( ) ;
v oi ddest r oy ( ) ;
v oi dst ack_ count ( ) ;
v oi dcr eat e( ) ;
i ntcount=0;
v oi dmai n( )
{
i ntno, ch, e;
pr i nt f ( " \ n1-Push" ) ;
pr i nt f ( " \ n2-Pop" ) ;
pr i nt f ( " \ n3-Top" ) ;
pr i nt f ( " \ n4-Empt y " ) ;
pr i nt f ( " \ n5-Exi t " ) ;
pr i nt f ( " \ n6-Di psl ay " ) ;
pr i nt f ( " \ n7-St ackCount " ) ;
pr i nt f ( " \ n8-Dest r oyst ack" ) ;
cr eat e( ) ;
whi l e( 1)
{
pr i nt f ( " \ nEnt erchoi ce: " ) ;
scanf ( " %d" , &ch) ;
swi t ch( ch)
{
case1:
pr i nt f ( " Ent erdat a: " ) ;
scanf ( " %d" , &no) ;
push( no) ;
br eak;
case2:
pop( ) ;
br eak;
case3:
i f( t op==NULL)
pr i nt f ( " Noel ement si nst ack" ) ;
el se
{
e=t opel ement ( ) ;
pr i nt f ( " \ nTopel ement: %d" , e) ;
}
br eak;
case4:
empt y ( ) ;
br eak;
case5:
exi t ( 0) ;
case6:
di spl ay ( ) ;
br eak;
case7:
st ack_ count ( ) ;
br eak;
case8:
dest r oy ( ) ;
br eak;
def aul t:
pr i nt f ( "Wr ongchoi ce, Pl easeent ercor r ectchoi ce" ) ;
br eak;
}
}
}
/ *Cr eat eempt yst ack* /
v oi dcr eat e( )
{
t op=NULL;
}
/ *Countst ackel ement s* /
v oi dst ack_ count ( )
{
pr i nt f ( " \ nNo.ofel ement si nst ack: %d" , count ) ;
}
/ *Pushdat ai nt ost ack* /
v oi dpush( i ntdat a)
{
i f( t op==NULL)
{
t op=( st r uctnode) mal l oc( 1si zeof ( st r uctnode) ) ;
t op>pt r=NULL;
t op>i nf o=dat a;
}
el se
{
t emp=( st r uctnode) mal l oc( 1si zeof ( st r uctnode) ) ;
t emp>pt r=t op;
t emp>i nf o=dat a;
t op=t emp;
}
count ++;
}
/ *Di spl ayst ackel ement s* /
v oi ddi spl ay ( )
{
t op1=t op;
i f( t op1==NULL)
{
pr i nt f ( " St acki sempt y " ) ;
r et ur n;
}
whi l e( t op1! =NULL)
{
pr i nt f ( " %d" , t op1>i nf o) ;
t op1=t op1>pt r ;
}
}
/ *PopOper at i ononst ack* /
v oi dpop( )
{
t op1=t op;
i f( t op1==NULL)
{
pr i nt f ( " \ nEr r or: Tr y i ngt opopf r omempt yst ack" ) ;
r et ur n;
}
el se
t op1=t op1>pt r ;
pr i nt f ( " \ nPoppedv al ue: %d" , t op>i nf o) ;
f r ee( t op) ;
t op=t op1;
count ;
}
/ *Ret ur nt opel ement* /
i ntt opel ement ( )
{
r et ur n( t op>i nf o) ;
}
/ *Checki fst acki sempt yornot* /
v oi dempt y ( )
{
i f( t op==NULL)
pr i nt f ( " \ nSt acki sempt y " ) ;
el se
pr i nt f ( " \ nSt acki snotempt ywi t h%del ement s" , count ) ;
}
/ *Dest r oyent i r est ack* /
v oi ddest r oy ( )
{
t op1=t op;
whi l e( t op1! =NULL)
{
t op1=t op>pt r ;
f r ee( t op) ;
t op=t op1;
t op1=t op1>pt r ;
f r ee( t op1) ;
t op=NULL;
pr i nt f ( " \ nAl l st ackel ement sdest r oy ed" ) ;
count=0;
}