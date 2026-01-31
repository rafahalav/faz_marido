document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('formCadastro');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Pegar dados do formulário
            const nome = form.nome.value;
            const whatsapp = form.whatsapp.value;
            const cidade = form.cidade.value;
            
            // Mensagem de sucesso
            alert('Cadastro enviado com sucesso! Entraremos em contato em breve pelo WhatsApp: ' + whatsapp);
            
            // Limpar formulário
            form.reset();
        });
    }
});