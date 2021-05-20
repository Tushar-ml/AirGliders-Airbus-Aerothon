but = document.getElementById('submit');
t = document.getElementById('msg_input');
messages= document.getElementById('messages');

but.addEventListener('click',(e)=>{
    e.preventDefault();
    console.log(t.value);
    const m = document.createElement("li");
    const u = document.createElement("li");

    //api call
    m.innerText = "Hi";
    u.innerText = t.value;
    $(u).css('list-style-type','none').css('margin-left','40px').css('font-size','20px');
    $(m).css('list-style-type','none').css('margin-left','350px').css('font-size','20px').css('margin-right','40px');
    messages.appendChild(u);
    messages.appendChild(m);
    t.value="";
});