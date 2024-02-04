import React from 'react';
import { fireEvent, getByLabelText, getByTestId, render, screen } from '@testing-library/react';
import App, { calcularNovoSaldo } from './App.js'
//import { act } from 'react-dom/test-utils';

describe('Componente principal ',() => {
    describe('Quando  eu abro o app  do banco ', () => {
        
        it('A Exebição do nome, do titulo', () => {
            render(<App />);
            expect(screen.getByText('ByteBank')).toBeInTheDocument();
        })

        it('verifica o saldo', ()=> {
            render(<App />);
            expect(screen.getByText('Saldo:')).toBeInTheDocument();
        })
        
        it('Quando abro o app, verifica o botão aparece', () => {
            render(<App />);
            expect (screen.getByText('Realizar operação')).toBeInTheDocument();
        })

    describe('Quando eu realizo uma transação', () => {
        it('que é um saque, o valor vai diminuir', () => {
            const valores = {
                transacao : 'saque',
                valor:50
            }
            const novoSaldo = calcularNovoSaldo(valores,150);
            expect(novoSaldo).toBe(100);
         })
        it('que é um saque,  a transação deve ser realizada', () => {
            
            render(<App />);
            
            const saldo = screen.getByText( 'R$ 1000' );
            const transacao = screen.getByLabelText('Saque');
            const valor = screen.getByTestId('valor');
            const botaoTransacao = screen.getByText('Realizar operação');

            expect(saldo.textContent).toBe('R$ 1000');
            
            fireEvent.click(transacao, {target: { value : 'saque' }})
            fireEvent.change(valor, {target: {value : 10}})
            fireEvent.click(botaoTransacao)

            expect(saldo.textContent).toBe('R$ 990');

            })
        })
    })     
})
