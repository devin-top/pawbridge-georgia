// Public contact email is linked directly in the Contact section above.

    const menuToggle = document.querySelector('.menu-toggle');
    const mobileNav = document.getElementById('mobile-nav');
    function closeMenu(){mobileNav.classList.remove('open');menuToggle.setAttribute('aria-expanded','false');menuToggle.setAttribute('aria-label','Open menu');}
    menuToggle.addEventListener('click',()=>{const isOpen=mobileNav.classList.toggle('open');menuToggle.setAttribute('aria-expanded',String(isOpen));menuToggle.setAttribute('aria-label',isOpen?'Close menu':'Open menu');});
    mobileNav.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
    document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});
    document.addEventListener('click',e=>{if(!e.target.closest('.header'))closeMenu()});

    const filters=[...document.querySelectorAll('.filter')];
    const items=[...document.querySelectorAll('.work-item')];
    filters.forEach(button=>button.addEventListener('click',()=>{const filter=button.dataset.filter;filters.forEach(b=>{const selected=b===button;b.classList.toggle('active',selected);b.setAttribute('aria-pressed',String(selected))});items.forEach(item=>{item.hidden=filter!=='all'&&item.dataset.category!==filter})}));

    document.getElementById('year').textContent=new Date().getFullYear();
