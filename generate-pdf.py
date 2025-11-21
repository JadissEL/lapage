#!/usr/bin/env python3
"""
Script pour générer le PDF du rapport PFE RoSiStrat avec haute qualité
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

async def generate_pdf():
    """Génère le PDF du rapport avec Playwright"""
    
    # Chemins
    current_dir = Path(__file__).parent
    html_file = current_dir / "rapport.html"
    output_pdf = current_dir / "Rapport_PFE_RoSiStrat_Jadiss_EL_ANTAKI.pdf"
    
    if not html_file.exists():
        print(f"❌ Erreur: {html_file} n'existe pas")
        return
    
    print("🚀 Démarrage de la génération du PDF...")
    print(f"📄 Fichier source: {html_file}")
    print(f"💾 Fichier de sortie: {output_pdf}")
    
    async with async_playwright() as p:
        # Lancer le navigateur
        print("🌐 Lancement du navigateur Chromium...")
        browser = await p.chromium.launch(
            headless=True,
            args=['--disable-web-security', '--disable-features=IsolateOrigins,site-per-process']
        )
        
        page = await browser.new_page(
            viewport={'width': 1200, 'height': 800},
            device_scale_factor=2  # Haute résolution
        )
        
        # Charger la page HTML
        print("📖 Chargement du rapport HTML...")
        file_url = f"file://{html_file.absolute()}"
        await page.goto(file_url, wait_until="networkidle", timeout=60000)
        
        # Attendre que toutes les images soient chargées
        print("🖼️  Chargement des images...")
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(2)  # Attendre un peu plus pour les images
        
        # Masquer les éléments non imprimables
        await page.evaluate("""
            () => {
                const noPrintElements = document.querySelectorAll('.no-print');
                noPrintElements.forEach(el => el.style.display = 'none');
            }
        """)
        
        # Générer le PDF
        print("📝 Génération du PDF en cours...")
        await page.pdf(
            path=str(output_pdf),
            format='A4',
            print_background=True,
            display_header_footer=False,
            margin={
                'top': '0mm',
                'right': '0mm',
                'bottom': '0mm',
                'left': '0mm'
            },
            prefer_css_page_size=True,
            scale=1.0
        )
        
        await browser.close()
        
        # Vérifier la taille du fichier
        file_size = output_pdf.stat().st_size / (1024 * 1024)  # En Mo
        print(f"✅ PDF généré avec succès!")
        print(f"📊 Taille du fichier: {file_size:.2f} Mo")
        print(f"📁 Emplacement: {output_pdf}")

if __name__ == "__main__":
    try:
        asyncio.run(generate_pdf())
    except KeyboardInterrupt:
        print("\n⚠️  Génération annulée par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
