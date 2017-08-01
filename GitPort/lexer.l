%{
	char string_table[]=" ";
	int yylval;
        int yyline=1;
        int yycolumn =1;

%}
inttoken [0-9]+

%%
<<EOF>> return 0;
";"	{yycolumn++;return 1;}
"("	{yycolumn++;return 2;}
")"	{yycolumn++;return 3;}
{inttoken}     {yycolumn+=strlen(yytext);yylval= atoi(yytext);return 4;}
begin	{yycolumn+=5;return 5;}
program {yycolumn+=7;return 6;}
"-"	{yycolumn++;return 7;}
"*"	{yycolumn++;return 8;}
var {yycolumn+=3;return 9;}
","	{yycolumn++;return 10;}
end {yycolumn+=3;return 12;}
is {yycolumn+=2;return 13;}
print {yycolumn+=5;return 16;}
div {yycolumn+=3;return 15;}
"+" {return 14;}
"=" {return 17;}
[a-zA-Z][a-zA-Z_0-9]* {yycolumn+=strlen(yytext);put_string(yytext);return 11;}
" " {yycolumn++;}
\n {yyline++;yycolumn=1;}
. {printf("Unrecognized character %s at Line : %d Column : %d \n",yytext,yyline,yycolumn);yycolumn++;}
%%


int put_string(char* image, int length)
{
    yylval = strlen(string_table);
    
    strcat(string_table,image);
    string_table[strlen(string_table)] = '\0';
	   
    return 0;
}



