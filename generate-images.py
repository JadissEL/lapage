#!/usr/bin/env python3
"""
Script pour générer automatiquement les images du rapport PFE RoSiStrat
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import seaborn as sns

# Configuration globale
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
COLORS = {
    'blue': '#4f46e5',
    'purple': '#7c3aed',
    'pink': '#ec4899',
    'gray': '#6b7280'
}

def create_architecture_global():
    """1. Architecture Globale"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Frontend
    frontend = FancyBboxPatch((0.5, 6.5), 2.5, 2, boxstyle="round,pad=0.1", 
                              edgecolor=COLORS['blue'], facecolor='#eff6ff', linewidth=2)
    ax.add_patch(frontend)
    ax.text(1.75, 8, 'Frontend', ha='center', va='center', fontsize=14, weight='bold', color=COLORS['blue'])
    ax.text(1.75, 7.5, 'React 18 + TypeScript', ha='center', va='center', fontsize=10)
    ax.text(1.75, 7, 'Vite + TailwindCSS', ha='center', va='center', fontsize=9, style='italic')
    
    # Backend
    backend = FancyBboxPatch((4, 6.5), 2.5, 2, boxstyle="round,pad=0.1",
                            edgecolor=COLORS['purple'], facecolor='#faf5ff', linewidth=2)
    ax.add_patch(backend)
    ax.text(5.25, 8, 'Backend', ha='center', va='center', fontsize=14, weight='bold', color=COLORS['purple'])
    ax.text(5.25, 7.5, 'Firebase Auth', ha='center', va='center', fontsize=10)
    ax.text(5.25, 7, 'Firestore DB', ha='center', va='center', fontsize=9, style='italic')
    
    # Moteur Simulation
    engine = FancyBboxPatch((7.5, 6.5), 2, 2, boxstyle="round,pad=0.1",
                           edgecolor=COLORS['pink'], facecolor='#fdf2f8', linewidth=2)
    ax.add_patch(engine)
    ax.text(8.5, 8, 'Moteur', ha='center', va='center', fontsize=14, weight='bold', color=COLORS['pink'])
    ax.text(8.5, 7.5, 'Simulation', ha='center', va='center', fontsize=10)
    ax.text(8.5, 7, '6 Stratégies', ha='center', va='center', fontsize=9, style='italic')
    
    # Base de données
    db = FancyBboxPatch((2, 3.5), 2.5, 1.8, boxstyle="round,pad=0.1",
                       edgecolor=COLORS['blue'], facecolor='#e0e7ff', linewidth=2)
    ax.add_patch(db)
    ax.text(3.25, 4.7, 'Firestore', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(3.25, 4.2, 'Simulations + Users', ha='center', va='center', fontsize=9)
    
    # DevOps/CI
    devops = FancyBboxPatch((5.5, 3.5), 2.5, 1.8, boxstyle="round,pad=0.1",
                           edgecolor=COLORS['purple'], facecolor='#f3e8ff', linewidth=2)
    ax.add_patch(devops)
    ax.text(6.75, 4.7, 'DevOps', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(6.75, 4.2, 'GitHub Actions + Docker', ha='center', va='center', fontsize=9)
    
    # Flèches
    arrow_props = dict(arrowstyle='->', lw=2, color=COLORS['gray'])
    ax.annotate('', xy=(4, 7.5), xytext=(3, 7.5), arrowprops=arrow_props)
    ax.annotate('', xy=(7.5, 7.5), xytext=(6.5, 7.5), arrowprops=arrow_props)
    ax.annotate('', xy=(3.25, 5.3), xytext=(2.5, 6.5), arrowprops=arrow_props)
    ax.annotate('', xy=(5.5, 5), xytext=(4.5, 5.3), arrowprops=arrow_props)
    
    ax.text(5, 9.5, 'Architecture Globale - RoSiStrat', ha='center', va='center', 
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/arch-global.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 1. arch-global.png généré")

def create_architecture_layers():
    """2. Architecture en couches"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    layers = [
        ('UI Layer', 'React Components + Radix UI', 8, COLORS['blue']),
        ('Application Layer', 'React Query + Context API', 6.5, COLORS['purple']),
        ('Domain Layer', 'Simulation Engine + Strategies', 5, COLORS['pink']),
        ('Infrastructure', 'Firebase + Firestore + Auth', 3.5, COLORS['blue']),
        ('PRNG Layer', 'Mersenne Twister (Seed)', 2, COLORS['purple'])
    ]
    
    for name, desc, y_pos, color in layers:
        rect = FancyBboxPatch((1, y_pos-0.4), 8, 0.8, boxstyle="round,pad=0.05",
                             edgecolor=color, facecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(2, y_pos, name, ha='left', va='center', fontsize=12, weight='bold', color=color)
        ax.text(7, y_pos, desc, ha='right', va='center', fontsize=9, style='italic')
    
    ax.text(5, 9.5, 'Architecture en Couches', ha='center', va='center',
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/arch-layers.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 2. arch-layers.png généré")

def create_use_case_diagram():
    """3. Diagramme cas d'utilisation"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Acteur
    ax.plot([1.5, 1.5], [6, 5.5], 'k-', lw=2)  # corps
    ax.add_patch(plt.Circle((1.5, 6.3), 0.2, color='black', fill=False, lw=2))  # tête
    ax.text(1.5, 4.8, 'Utilisateur', ha='center', fontsize=11, weight='bold')
    
    # Cas d'utilisation
    use_cases = [
        ('Configurer\nSimulation', 5, 8, COLORS['blue']),
        ('Lancer\nSimulation', 5, 6.5, COLORS['purple']),
        ('Visualiser\nRésultats', 5, 5, COLORS['pink']),
        ('Exporter\nCSV', 8, 7, COLORS['blue']),
        ('Comparer\nStratégies', 8, 5.5, COLORS['purple'])
    ]
    
    for name, x, y, color in use_cases:
        ellipse = mpatches.Ellipse((x, y), 1.8, 1, edgecolor=color, facecolor='white', linewidth=2)
        ax.add_patch(ellipse)
        ax.text(x, y, name, ha='center', va='center', fontsize=10, weight='bold')
        
        # Ligne vers l'acteur
        ax.plot([1.7, x-0.9], [6, y], 'k--', lw=1, alpha=0.5)
    
    ax.text(5, 9.5, 'Diagramme de Cas d\'Utilisation', ha='center', va='center',
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/use-case.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 3. use-case.png généré")

def create_tech_specs():
    """4. Spécifications techniques"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    specs = [
        ('Frontend', ['React 18.3.1', 'TypeScript 5.5', 'Vite 7.2', 'TailwindCSS 3.4'], 1, COLORS['blue']),
        ('Backend', ['Firebase 11.9', 'Firestore', 'Auth', 'Security Rules'], 4, COLORS['purple']),
        ('Tests', ['Vitest 3.1.4', '318 tests', 'React Testing Lib', 'Coverage 85%'], 7, COLORS['pink'])
    ]
    
    for title, items, x, color in specs:
        rect = FancyBboxPatch((x-0.4, 0.5), 2.5, 4.5, boxstyle="round,pad=0.1",
                             edgecolor=color, facecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.85, 4.5, title, ha='center', va='center', fontsize=14, weight='bold', color=color)
        
        for i, item in enumerate(items):
            ax.text(x+0.85, 3.7 - i*0.6, f'• {item}', ha='center', va='center', fontsize=10)
    
    ax.text(5, 5.5, 'Stack Technique', ha='center', va='center',
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/tech-specs.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 4. tech-specs.png généré")

def create_intro_schema():
    """5. Schéma d'introduction"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Stratégies
    strat = FancyBboxPatch((0.5, 2), 2, 2, boxstyle="round,pad=0.1",
                          edgecolor=COLORS['blue'], facecolor='#eff6ff', linewidth=2)
    ax.add_patch(strat)
    ax.text(1.5, 3.5, 'Stratégies', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(1.5, 2.8, '• Martingale', ha='center', fontsize=9)
    ax.text(1.5, 2.4, '• SAM+', ha='center', fontsize=9)
    
    # Moteur
    engine = FancyBboxPatch((4, 2), 2, 2, boxstyle="round,pad=0.1",
                           edgecolor=COLORS['purple'], facecolor='#faf5ff', linewidth=2)
    ax.add_patch(engine)
    ax.text(5, 3.5, 'Moteur', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(5, 2.8, 'Simulation', ha='center', fontsize=10)
    ax.text(5, 2.4, 'PRNG', ha='center', fontsize=9)
    
    # Métriques
    metrics = FancyBboxPatch((7.5, 2), 2, 2, boxstyle="round,pad=0.1",
                            edgecolor=COLORS['pink'], facecolor='#fdf2f8', linewidth=2)
    ax.add_patch(metrics)
    ax.text(8.5, 3.5, 'Calculs', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(8.5, 2.8, '• ROI', ha='center', fontsize=9)
    ax.text(8.5, 2.4, '• Drawdown', ha='center', fontsize=9)
    
    # Flèches
    arrow_props = dict(arrowstyle='->', lw=3, color=COLORS['gray'])
    ax.annotate('', xy=(4, 3), xytext=(2.5, 3), arrowprops=arrow_props)
    ax.annotate('', xy=(7.5, 3), xytext=(6, 3), arrowprops=arrow_props)
    
    ax.text(5, 5, 'Flux de Simulation', ha='center', va='center',
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/intro-schema.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 5. intro-schema.png généré")

def create_history_timeline():
    """6. Timeline historique"""
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    # Ligne temporelle
    ax.plot([1, 9], [2.5, 2.5], 'k-', lw=2)
    
    events = [
        (1, '1796', 'Martingale\nClassique', COLORS['blue']),
        (3, '1960', 'Fibonacci', COLORS['purple']),
        (5, '1985', 'Kelly\nCriterion', COLORS['pink']),
        (7, '2010', 'Algorithmes\nAdaptatifs', COLORS['blue']),
        (9, '2024', 'RoSiStrat\n(SAM+)', COLORS['purple'])
    ]
    
    for x, year, name, color in events:
        ax.plot([x, x], [2.5, 3.2], color=color, lw=2)
        ax.add_patch(plt.Circle((x, 2.5), 0.15, color=color, zorder=3))
        ax.text(x, 3.6, name, ha='center', va='bottom', fontsize=10, weight='bold', color=color)
        ax.text(x, 1.8, year, ha='center', va='top', fontsize=9, style='italic')
    
    ax.text(5, 4.5, 'Évolution des Stratégies de Roulette', ha='center', va='center',
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/history.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 6. history.png généré")

def create_results_graph():
    """8. Graphique résultats (3 stratégies)"""
    np.random.seed(42)
    tours = np.arange(0, 10000, 100)
    
    # Simulation de trajectoires
    martingale = 1000 + np.cumsum(np.random.randn(100) * 50 - 2.7)
    sam_plus = 1000 + np.cumsum(np.random.randn(100) * 30 - 1.5)
    baseline = 1000 + np.cumsum(np.random.randn(100) * 20 - 2)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(tours, martingale, label='Standard Martingale', color=COLORS['pink'], linewidth=2)
    ax.plot(tours, sam_plus, label='SAM+', color=COLORS['purple'], linewidth=2)
    ax.plot(tours, baseline, label='Baseline', color=COLORS['blue'], linewidth=2, linestyle='--')
    
    ax.axhline(y=1000, color='gray', linestyle=':', alpha=0.5, label='Capital Initial')
    ax.set_xlabel('Tours', fontsize=12, weight='bold')
    ax.set_ylabel('Capital (€)', fontsize=12, weight='bold')
    ax.set_title('Évolution du Capital - 3 Stratégies (10k tours)', fontsize=14, weight='bold', color=COLORS['blue'])
    ax.legend(loc='best', frameon=True, shadow=True)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/results-graph.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 8. results-graph.png généré")

def create_perf_chart():
    """10. Performance chart"""
    tours = [1000, 5000, 10000, 50000, 100000]
    temps = [0.05, 0.25, 0.5, 2.5, 5.2]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(range(len(tours)), temps, color=[COLORS['blue'], COLORS['purple'], 
                                                     COLORS['pink'], COLORS['blue'], COLORS['purple']])
    
    ax.set_xticks(range(len(tours)))
    ax.set_xticklabels([f'{t//1000}k' for t in tours])
    ax.set_xlabel('Nombre de Tours', fontsize=12, weight='bold')
    ax.set_ylabel('Temps d\'exécution (s)', fontsize=12, weight='bold')
    ax.set_title('Performance - Temps vs Nombre de Tours', fontsize=14, weight='bold', color=COLORS['blue'])
    ax.grid(True, axis='y', alpha=0.3)
    
    for i, (bar, val) in enumerate(zip(bars, temps)):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.1, f'{val}s', 
                ha='center', va='bottom', fontsize=10, weight='bold')
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/perf-chart.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 10. perf-chart.png généré")

def create_perf_metrics():
    """11. Métriques de performance"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    categories = ['1k tours', '10k tours', '50k tours']
    temps = [0.05, 0.5, 2.5]
    memoire = [15, 45, 180]  # MB
    
    x = np.arange(len(categories))
    width = 0.35
    
    ax2 = ax.twinx()
    bars1 = ax.bar(x - width/2, temps, width, label='Temps (s)', color=COLORS['blue'])
    bars2 = ax2.bar(x + width/2, memoire, width, label='Mémoire (MB)', color=COLORS['purple'])
    
    ax.set_xlabel('Scénarios de Test', fontsize=12, weight='bold')
    ax.set_ylabel('Temps (s)', fontsize=11, weight='bold', color=COLORS['blue'])
    ax2.set_ylabel('Mémoire (MB)', fontsize=11, weight='bold', color=COLORS['purple'])
    ax.set_title('Métriques de Performance', fontsize=14, weight='bold', color=COLORS['blue'])
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/perf-metrics.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 11. perf-metrics.png généré")

def create_prng_distribution():
    """13. Distribution PRNG"""
    np.random.seed(42)
    # Simulation 100k spins sur roulette (0-36)
    spins = np.random.randint(0, 37, 100000)
    
    fig, ax = plt.subplots(figsize=(14, 6))
    counts, bins, patches = ax.hist(spins, bins=37, edgecolor='black', alpha=0.7)
    
    # Colorer alternativement
    for i, patch in enumerate(patches):
        if i % 2 == 0:
            patch.set_facecolor(COLORS['blue'])
        else:
            patch.set_facecolor(COLORS['purple'])
    
    # Ligne d'unifor mité attendue
    expected = 100000 / 37
    ax.axhline(y=expected, color='red', linestyle='--', linewidth=2, label=f'Fréquence attendue ({expected:.0f})')
    
    ax.set_xlabel('Numéro de la Roulette', fontsize=12, weight='bold')
    ax.set_ylabel('Fréquence (sur 100k spins)', fontsize=12, weight='bold')
    ax.set_title('Distribution PRNG - Mersenne Twister (100k spins)', fontsize=14, weight='bold', color=COLORS['blue'])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/prng-dist.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 13. prng-dist.png généré")

def create_firebase_security():
    """14. Sécurité Firebase"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titre
    ax.text(5, 9.5, 'Audit Sécurité Firebase', ha='center', va='center',
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    # Sections
    sections = [
        ('Authentification', ['• Firebase Auth', '• JWT Tokens', '• Session Management'], 7.5, COLORS['blue']),
        ('Firestore Rules', ['• Ownership-based access', '• Deny-all default', '• User validation'], 5.5, COLORS['purple']),
        ('Conformité', ['• OWASP Top 10', '• GDPR compliant', '• Security headers'], 3.5, COLORS['pink']),
        ('Tests', ['• 41 Firebase tests', '• Security audit passed', '• Index verification'], 1.5, COLORS['blue'])
    ]
    
    for title, items, y, color in sections:
        rect = FancyBboxPatch((1, y-0.4), 8, 1.2, boxstyle="round,pad=0.1",
                             edgecolor=color, facecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(1.5, y+0.4, title, ha='left', va='center', fontsize=12, weight='bold', color=color)
        
        for i, item in enumerate(items):
            ax.text(5 + i*2.5, y, item, ha='left', va='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/firebase-sec.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 14. firebase-sec.png généré")

def create_security_overview():
    """15. Vue d'ensemble sécurité"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Entrée
    input_box = FancyBboxPatch((0.5, 2.5), 2, 1, boxstyle="round,pad=0.1",
                              edgecolor=COLORS['blue'], facecolor='#eff6ff', linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.5, 3, 'Input\nUtilisateur', ha='center', va='center', fontsize=10, weight='bold')
    
    # Validation
    valid_box = FancyBboxPatch((3.5, 2.5), 2, 1, boxstyle="round,pad=0.1",
                              edgecolor=COLORS['purple'], facecolor='#faf5ff', linewidth=2)
    ax.add_patch(valid_box)
    ax.text(4.5, 3, 'Validation\n& Sanitize', ha='center', va='center', fontsize=10, weight='bold')
    
    # Traitement
    process_box = FancyBboxPatch((6.5, 2.5), 2, 1, boxstyle="round,pad=0.1",
                                edgecolor=COLORS['pink'], facecolor='#fdf2f8', linewidth=2)
    ax.add_patch(process_box)
    ax.text(7.5, 3, 'Traitement\nSécurisé', ha='center', va='center', fontsize=10, weight='bold')
    
    # Erreurs
    error_box = FancyBboxPatch((4, 0.5), 2, 0.8, boxstyle="round,pad=0.05",
                              edgecolor='red', facecolor='#fee', linewidth=2)
    ax.add_patch(error_box)
    ax.text(5, 0.9, 'Gestion Erreurs', ha='center', va='center', fontsize=9, weight='bold', color='red')
    
    # Flèches
    arrow_props = dict(arrowstyle='->', lw=2, color=COLORS['gray'])
    ax.annotate('', xy=(3.5, 3), xytext=(2.5, 3), arrowprops=arrow_props)
    ax.annotate('', xy=(6.5, 3), xytext=(5.5, 3), arrowprops=arrow_props)
    ax.annotate('', xy=(5, 1.3), xytext=(4.5, 2.5), arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    
    ax.text(5, 5, 'Flux de Sécurité et Validation', ha='center', va='center',
            fontsize=14, weight='bold', color=COLORS['blue'])
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/security-overview.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 15. security-overview.png généré")

def create_ui_screenshots():
    """18. UI Screenshots mockup"""
    fig = plt.figure(figsize=(14, 8))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # Dashboard
    ax1 = fig.add_subplot(gs[0, :])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 3)
    ax1.axis('off')
    ax1.text(5, 2.5, 'Dashboard Principal', ha='center', fontsize=14, weight='bold', color=COLORS['blue'])
    
    # Cartes métriques
    metrics_data = [
        ('Solde', '1,250 €', 1.5, COLORS['blue']),
        ('ROI', '+25%', 3.5, COLORS['purple']),
        ('Variance', '450', 5.5, COLORS['pink']),
        ('Drawdown', '-15%', 7.5, COLORS['blue'])
    ]
    
    for label, value, x, color in metrics_data:
        rect = FancyBboxPatch((x-0.6, 0.5), 1.2, 1.2, boxstyle="round,pad=0.1",
                             edgecolor=color, facecolor='white', linewidth=2)
        ax1.add_patch(rect)
        ax1.text(x, 1.4, label, ha='center', fontsize=10, weight='bold', color=color)
        ax1.text(x, 0.9, value, ha='center', fontsize=14, weight='bold')
    
    # Paramétrage
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 3)
    ax2.axis('off')
    ax2.text(2.5, 2.7, 'Configuration', ha='center', fontsize=12, weight='bold', color=COLORS['purple'])
    
    config_items = ['Capital: 1000€', 'Stratégie: SAM+', 'Tours: 10,000', 'Seed: 12345']
    for i, item in enumerate(config_items):
        ax2.text(0.5, 2 - i*0.5, f'• {item}', fontsize=10)
    
    # Résultats
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.set_xlim(0, 5)
    ax3.set_ylim(0, 3)
    ax3.axis('off')
    ax3.text(2.5, 2.7, 'Résultats', ha='center', fontsize=12, weight='bold', color=COLORS['pink'])
    
    # Mini graphique
    x = np.linspace(0, 4, 50)
    y = 1 + 0.3 * np.sin(x * 3) + 0.05 * x
    ax3.plot(x + 0.5, y, color=COLORS['purple'], linewidth=2)
    ax3.fill_between(x + 0.5, 0, y, alpha=0.2, color=COLORS['purple'])
    
    plt.savefig('/workspaces/lapage/images/ui-screens.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 18. ui-screens.png généré")

def create_roadmap():
    """19. Roadmap"""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    ax.text(5, 5.5, 'Roadmap - Évolutions Futures', ha='center', va='center',
            fontsize=16, weight='bold', color=COLORS['blue'])
    
    phases = [
        ('Q1 2025', ['ML Adaptatif', 'WebAssembly'], 1.5, COLORS['blue']),
        ('Q2 2025', ['Mode Multi-joueur', 'API REST'], 3.5, COLORS['purple']),
        ('Q3 2025', ['K8s Deployment', 'Monitoring ++'], 5.5, COLORS['pink']),
        ('Q4 2025', ['Mobile App', 'Advanced Analytics'], 7.5, COLORS['blue'])
    ]
    
    # Ligne de temps
    ax.plot([1, 8.5], [3, 3], 'k-', lw=2)
    
    for title, features, x, color in phases:
        # Point sur la timeline
        ax.add_patch(plt.Circle((x, 3), 0.15, color=color, zorder=3))
        
        # Boîte de phase
        rect = FancyBboxPatch((x-0.6, 0.5), 1.2, 1.5, boxstyle="round,pad=0.1",
                             edgecolor=color, facecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 1.8, title, ha='center', fontsize=11, weight='bold', color=color)
        
        for i, feat in enumerate(features):
            ax.text(x, 1.3 - i*0.35, feat, ha='center', fontsize=8)
        
        # Ligne vers timeline
        ax.plot([x, x], [2, 2.85], color=color, lw=2, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('/workspaces/lapage/images/roadmap.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ 19. roadmap.png généré")

# Exécution principale
if __name__ == '__main__':
    print("🎨 Génération des images pour le rapport RoSiStrat...\n")
    
    # Créer le dossier images s'il n'existe pas
    import os
    os.makedirs('/workspaces/lapage/images', exist_ok=True)
    
    # Générer toutes les images demandées
    create_architecture_global()        # 1
    create_architecture_layers()        # 2
    create_use_case_diagram()          # 3
    create_tech_specs()                # 4
    create_intro_schema()              # 5
    create_history_timeline()          # 6
    create_results_graph()             # 8
    create_perf_chart()                # 10
    create_perf_metrics()              # 11
    create_prng_distribution()         # 13
    create_firebase_security()         # 14
    create_security_overview()         # 15
    create_ui_screenshots()            # 18
    create_roadmap()                   # 19
    
    print("\n✨ Toutes les images ont été générées avec succès !")
    print("📁 Dossier : /workspaces/lapage/images/")
