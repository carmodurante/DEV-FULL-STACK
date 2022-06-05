// Programa para somar todos numeros primos até o numero digitado.
// Autor: Carmo Durante Neto

programa {
	funcao inicio() {
	    
		inteiro divisores = 0, numero, contador, contador2, soma = 0, resto
		
		escreva("Digite um numero inteiro: ")
		leia(numero)
		
		se(numero > 0)
		{
    		para (contador = 1; contador <= numero; contador ++) 
    		{
    		    
    		    contador2 = 1
    		    divisores = 0
    		    
    		    faca   
                {  
                    resto = contador%contador2
                    
                    se (resto == 0)
                    {
                        divisores = divisores + 1
                    } 
                    
                    contador2 = contador2 + 1
                    
                } enquanto (contador2 <= contador)  
                
    		    se (divisores == 2 )
    		    {
    		       escreva("\nO numero ",contador," é primo!\n")
    		       soma = soma + contador
    		    }
    		}
    	}
    	
    	 escreva("\nA soma de todos os numeros primos menores ou iguais a: ", numero," é: ", soma, "\n")
    	 
	   }
    }

