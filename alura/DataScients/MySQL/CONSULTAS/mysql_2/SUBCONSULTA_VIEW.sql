SELECT DISTINCT BAIRRO FROM tabela_de_vendedores;
SELECT * FROM tabela_de_clientes WHERE BAIRRO IN ('tijuca','Jardins','CopaCabana');
SELECT * FROM tabela_de_clientes WHERE BAIRRO IN (SELECT DISTINCT BAIRRO FROM tabela_de_vendedores);

SELECT X.EMBALAGEM,X.PRECO_MAXIMO FROM
-- CHAMOU TUDO DE X
(SELECT EMBALAGEM,MAX(PRECO_DE_LISTA) AS PRECO_MAXIMO FROM tabela_de_produtos GROUP BY EMBALAGEM) X 
 WHERE X.PRECO_MAXIMO >= 10;
  
 -- VIEW
 SELECT X.EMBALAGEM,X.PRECO_MAXIMO FROM
VW_MAIORES_EMBALAGENS X  WHERE X.PRECO_MAXIMO >= 10;

SELECT A.NOME_DO_PRODUTO,A.EMBALAGEM,A.PRECO_DE_LISTA,X.PRECO_MAXIMO,
(A.PRECO_DE_LISTA/X.PRECO_MAXIMO -1)*100 AS PERCENTUAL
FROM tabela_de_produtos A INNER JOIN VW_MAIORES_EMBALAGENS X
ON A.EMBALAGEM = X.EMBALAGEM