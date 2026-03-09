import os
import glob
import re

new_footer = """            <footer class="bg-primary text-white pt-16 pb-24 md:py-16 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-5"></div>
                <div class="max-w-7xl mx-auto px-6 lg:px-20 relative z-10 text-center md:text-left">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-10 md:gap-12 border-b border-white/10 pb-12">
                        <div class="col-span-1 md:col-span-2 space-y-6 flex flex-col items-center md:items-start">
                            <div class="flex items-center justify-center md:justify-start gap-3 group cursor-pointer w-full">
                                <img src="../img/cerebro.png" alt="Neuropsicóloga Rodríguez" class="h-10 w-auto object-contain brain-shine filter drop-shadow-[0_0_8px_rgba(255,255,255,0.2)]" />
                                <h2 class="text-white text-xl md:text-xl font-extrabold font-display tracking-tight transition-colors duration-300 group-hover:text-accent-light">
                                    Neuropsicóloga Rodríguez</h2>
                            </div>
                            <p class="text-slate-300 max-w-sm leading-relaxed text-sm md:text-base mx-auto md:mx-0">
                                Transformando vidas a través de la neurociencia y la empatía clínica. Tu salud mental es nuestra prioridad.
                            </p>
                        </div>
                        <div class="flex flex-col items-center md:items-start w-full">
                            <h5 class="font-bold mb-4 md:mb-6 text-accent flex flex-col items-center md:items-start gap-2">
                                <span class="w-8 h-1 bg-accent/50 rounded-full md:hidden"></span>
                                Navegación
                            </h5>
                            <ul class="space-y-4 text-slate-300 w-full flex flex-col items-center md:items-start">
                                <li><a class="hover:text-white transition-colors flex items-center justify-center md:justify-start gap-2 w-full"
                                        href="index.html"><span class="w-1.5 h-1.5 rounded-full bg-accent hidden md:block"></span>Inicio</a></li>
                                <li><a class="hover:text-white transition-colors flex items-center justify-center md:justify-start gap-2 w-full"
                                        href="sobremi.html"><span class="w-1.5 h-1.5 rounded-full bg-accent hidden md:block"></span>Sobre Mí</a></li>
                                <li><a class="hover:text-white transition-colors flex items-center justify-center md:justify-start gap-2 w-full"
                                        href="cortexa.html"><span class="w-1.5 h-1.5 rounded-full bg-accent hidden md:block"></span>Cortexa</a></li>
                                <li><a class="hover:text-white transition-colors flex items-center justify-center md:justify-start gap-2 w-full"
                                        href="especialidades.html"><span class="w-1.5 h-1.5 rounded-full bg-accent hidden md:block"></span> Especialidades</a></li>
                                <li><a class="hover:text-white transition-colors flex items-center justify-center md:justify-start gap-2 w-full"
                                        href="reservarcita.html"><span class="w-1.5 h-1.5 rounded-full bg-accent hidden md:block"></span> Reservar Cita</a></li>
                            </ul>
                        </div>
                        <div class="flex flex-col items-center md:items-start w-full mt-6 md:mt-0">
                            <h5 class="font-bold mb-4 md:mb-6 text-accent flex flex-col items-center md:items-start gap-2">
                                <span class="w-8 h-1 bg-accent/50 rounded-full md:hidden"></span>
                                Contacto
                            </h5>
                            <ul class="space-y-4 text-slate-300 w-full flex flex-col items-center md:items-start">
                                <li class="flex flex-col md:flex-row items-center md:items-start justify-center md:justify-start gap-2 md:gap-3 text-center md:text-left w-full">
                                    <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-sm">mail</span>
                                    </div>
                                    <span class="break-words sm:break-all md:break-words w-full text-sm md:text-base leading-tight md:leading-normal mt-1 md:mt-0">neuropsicologarodriguez@gmail.com</span>
                                </li>
                                <li class="flex flex-col md:flex-row items-center md:items-start justify-center md:justify-start gap-2 md:gap-3 text-center md:text-left w-full mt-2 md:mt-0">
                                    <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-sm">location_on</span>
                                    </div>
                                    <span class="text-sm md:text-base mt-1 md:mt-0">Lima, Perú</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="pt-8 md:pt-12 flex flex-col items-center md:items-center gap-6 text-slate-400 text-sm">
                        <div class="flex flex-col md:flex-row gap-4 justify-center items-center w-full">
                            <a class="w-full sm:w-auto px-6 py-3 md:px-4 md:py-2 rounded-xl bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white text-xs font-semibold tracking-wide border border-white/10 hover:border-white/20 transition-all duration-300 flex items-center justify-center gap-2 group backdrop-blur-sm shadow-sm"
                                href="privacidad.html">
                                <span class="material-symbols-outlined text-sm group-hover:scale-110 transition-transform text-accent-light">shield_lock</span>
                                Política de Privacidad
                            </a>
                            <a class="w-full sm:w-auto px-6 py-3 md:px-4 md:py-2 rounded-xl bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white text-xs font-semibold tracking-wide border border-white/10 hover:border-white/20 transition-all duration-300 flex items-center justify-center gap-2 group backdrop-blur-sm shadow-sm"
                                href="terminos.html">
                                <span class="material-symbols-outlined text-sm group-hover:scale-110 transition-transform text-accent-light">gavel</span>
                                Términos de Servicio
                            </a>
                        </div>
                        <p class="text-center w-full px-4 text-xs md:text-sm mt-2 md:mt-0 opacity-60">© 2024 Neuropsicóloga Rodríguez. Todos los derechos reservados.</p>
                    </div>
                </div>
            </footer>"""

html_files = [f for f in glob.glob("*.html")]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the entire footer block
    pattern = r'<footer class="bg-primary text-white p[yt]-[0-9]+.*?</footer>'
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, new_footer, content, flags=re.DOTALL)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Footer not found in {filename}")
