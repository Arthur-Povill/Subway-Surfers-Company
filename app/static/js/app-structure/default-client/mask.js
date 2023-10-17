if(document.querySelector('#phone')){
    function phone(v){
        if(v != ''){
            v=v.replace(/\D/g,"");
            v=v.replace(/(\d{2})(\d)/,"($1) $2");
            v=v.replace(/(\d{5})(\d)/,"$1-$2");
        }
        return v; 
    }
    document.querySelector('#phone').addEventListener('keypress', function(e) {
        e.target.value = phone(e.target.value);
    });
}


if(document.querySelector('#cep')){
    function cep(v){
        if(v != ''){
            v=v.replace(/\D/g,"");
            v=v.replace(/(\d{5})(\d)/,"$1-$2");
        }
        return v; 
    }
    document.querySelector('#cep').addEventListener('keypress', function(e) {
        e.target.value = cep(e.target.value);
    });
}



if(document.querySelector('#cpf')){
    function cpf(v){
        if(v != ''){
            v=v.replace(/\D/g,"");
            v=v.replace(/(\d{3})(\d)/,"$1.$2");
            v=v.replace(/(\d{3})(\d)/,"$1.$2");
            v=v.replace(/(\d{3})(\d{1,2})$/,"$1-$2");
        }
        return v; 
    }
    document.querySelector('#cpf').addEventListener('keypress', function(e) {
        e.target.value = cpf(e.target.value);
    });
}