// Script de génération PDF du rapport avec Puppeteer
// Usage: npm run pdf (génère rapport.pdf à partir de rapport.html)
import puppeteer from 'puppeteer';
import { readFile } from 'fs/promises';
import { resolve } from 'path';

async function main() {
  const htmlPath = resolve('rapport.html');
  const htmlContent = await readFile(htmlPath, 'utf8');
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  await page.setContent(htmlContent, {waitUntil: 'networkidle0'});
  await page.emulateMediaType('print');
  await page.pdf({
    path: 'rapport.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '20mm', bottom: '20mm', left: '18mm', right: '18mm' }
  });
  await browser.close();
  console.log('PDF généré: rapport.pdf');
}

main().catch(e=>{console.error(e);process.exit(1);});