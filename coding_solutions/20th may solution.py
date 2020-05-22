i mpor tj av a. ut i l . St ack;
/ /Dat aSt r uct ur et ost or eal i nkedl i stnode
cl assNode{
i ntdat a;
Nodenext ;
Node( i nti )
{
t hi s. dat a=i ;
t hi s. next=nul l ;
}
} ;
cl assMai n
{
/ /Funct i ont odet er mi nei fagi v enl i nkedl i sti spal i ndr omeornot
publ i cst at i cbool eani sPal i ndr ome( Nodehead)
{
/ /const r uctanempt yst ack
St ack<I nt eger >s=newSt ack<>( ) ;
/ /pushal l el ement soft hel i nkedl i sti nt ot hest ack
Nodenode=head;
whi l e( node! =nul l ){
s. push( node. dat a) ;
node=node. next ;
}
/ /t r av er set hel i nkedl i stagai n
node=head;
whi l e( node! =nul l )
{
/ /popt het opel ementf r omt hest ack
i ntt op=s. pop( ) ;
/ /compar et hepoppedel ementwi t hcur r entnode' sdat a
/ /r et ur nf al sei fmi smat chhappens
i f( t op! =node. dat a){
r et ur nf al se;
}
/ /adv ancet ot henextnode
node=node. next ;
}
/ /wer eachher eonl ywhent hel i nkedl i sti spal i ndr ome
r et ur nt r ue;
}
publ i cst at i cv oi dmai n( St r i ng[ ]ar gs)
{
Nodehead=newNode( 1) ;
head. next=newNode( 2) ;
head. next . next=newNode( 3) ;
head. next . next . next=newNode( 2) ;
head. next . next . next . next=newNode( 1) ;
i f( i sPal i ndr ome( head) ){
Sy st em. out . pr i nt ( " Li nkedLi sti sapal i ndr ome. " ) ;
}el se{
Sy st em. out . pr i nt ( " Li nkedLi sti snotapal i ndr ome. " ) ;
}
}
}