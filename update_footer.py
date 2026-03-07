import os
import re

dir_path = r'c:\Users\Leonardo\Desktop\LovePoints\NeuropsicologaRodriguez\nuevoFrontend'
files = ['nuevoIndex.html', 'nuevoSobremi.html', 'nuevoCortexa.html', 'nuevoEspecialidades.html', 'nuevoReservarcita.html']

new_buttons = """                        <div class="flex flex-wrap gap-4 mt-4 md:mt-0">
                            <a class="px-4 py-2 rounded-xl bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white text-xs font-semibold tracking-wide border border-white/10 hover:border-white/20 transition-all duration-300 flex items-center gap-2 group backdrop-blur-sm shadow-sm" href="nuevoPrivacidad.html">
                                <span class="material-symbols-outlined text-sm group-hover:scale-110 transition-transform text-accent-light">shield_lock</span>
                                Política de Privacidad
                            </a>
                            <a class="px-4 py-2 rounded-xl bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white text-xs font-semibold tracking-wide border border-white/10 hover:border-white/20 transition-all duration-300 flex items-center gap-2 group backdrop-blur-sm shadow-sm" href="nuevoTerminos.html">
                                <span class="material-symbols-outlined text-sm group-hover:scale-110 transition-transform text-accent-light">gavel</span>
                                Términos de Servicio
                            </a>
                        </div>"""

for fn in files:
    filepath = os.path.join(dir_path, fn)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We look for a <div ...> that contains "Política de Privacidad". Assuming it's inside the footer.
    # A generic regex to replace the container of the old links.
    # Pattern looks for `<div *(class="[^"]*")?>\s*<a[^>]*>Política.*?</a>\s*<a[^>]*>Términos.*?</a>\s*</div>`
    pattern = re.compile(r'<div[^>]*>\s*<a[^>]+>(?:Política|Politica).*?</a>\s*<a[^>]+>Términos.*?</a>\s*</div>', re.DOTALL | re.IGNORECASE)
    
    new_content, count = pattern.subn(new_buttons, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {fn}")
    else:
        print(f"Could not find the footer links in {fn}")
