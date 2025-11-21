#!/usr/bin/env python3
"""
Serveur Flask simple pour générer le PDF
"""

from flask import Flask, send_file, jsonify
from flask_cors import CORS
import subprocess
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    """Endpoint pour générer le PDF"""
    try:
        # Exécuter le script de génération
        result = subprocess.run(
            ['python3', 'generate-pdf.py'],
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            pdf_path = Path(__file__).parent / 'Rapport_PFE_RoSiStrat_Jadiss_EL_ANTAKI.pdf'
            if pdf_path.exists():
                return send_file(
                    pdf_path,
                    mimetype='application/pdf',
                    as_attachment=True,
                    download_name='Rapport_PFE_RoSiStrat_Jadiss_EL_ANTAKI.pdf'
                )
            else:
                return jsonify({'error': 'PDF non généré'}), 500
        else:
            return jsonify({'error': result.stderr}), 500
            
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout lors de la génération'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
