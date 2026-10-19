Cenário: Fluxo de compra

Como um usuário
Quero realizar o fluxo de compra de um produto
Para concluir uma compra com sucesso

Dado que o usuário possui acesso ao site
Quando o usuário acessa a Home
E clica na opção "catálogo" no navbar
Então o usuário é direcionado para a página Catálogo

Dado que o usuário acessou a página Catálogo
Quando o usuário seleciona um produto do 1ª step
E é direcionado para a PDP do produto
Então clica no btn “ADD TO CART”
E o produto é adicionado ao carrinho

Dado que o carrinho contém um produto
Quando clico no btn “CHECK OUT” que está o header
Então o usuário é direcionado para o carrinho

Dado que a página de checkout foi apresentada
E o produto selecionado permaneceu disponível no resumo da compra
Quando o usuário preenche os dados obrigatórios do endereço
E preenche os dados necessários para pagamento
E solicita a finalização da compra
Então a compra deve ser processada
E o resultado correspondente à transação deve ser apresentado