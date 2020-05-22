packageshor t est pal i ndr omeexampl e. j av a;
i mpor tj av a. ut i l . Scanner ;
publ i ccl assShor t est Pal i ndr omeDemo{
publ i cst at i cSt r i ngshor t est Pal i ndr ome( St r i ngst r ){
i ntx=0;
i nty =st r . l engt h( ) 1;
whi l e( y >=0) {
i f ( st r . char At ( x) ==st r . char At ( y ) ) {
x++;
}
y ;
}
i f ( x==st r . l engt h( ) )
r et ur nst r ;
St r i ngsuf f i x=st r . subst r i ng( x) ;
St r i ngpr ef i x=newSt r i ngBui l der ( suf f i x) . r ev er se( ) . t oSt r i ng( ) ;
St r i ngmi d=shor t est Pal i ndr ome( st r . subst r i ng( 0, x) ) ;
r et ur npr ef i x+mi d+suf f i x;
}
publ i cst at i cv oi dmai n( St r i ng[ ]ar gs)
{
Scanneri n=newScanner ( Sy st em. i n) ;
Sy st em. out . pr i nt l n( " Ent eraSt r i ngt of i ndoutshor t estpal i ndr ome" ) ;
St r i ngst r =i n. next Li ne( ) ;
Sy st em. out . pr i nt l n( " Shor t estpal i ndr omeof" +st r +"i s" +shor t est Pal i ndr ome( st r ) ) ;
}