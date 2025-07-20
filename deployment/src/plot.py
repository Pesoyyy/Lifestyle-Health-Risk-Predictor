import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('src/addiction_population_data.csv')

def eda1():
    """
    Visualisasi distribusi target (has_health_issues) dan menampilkan proporsi
    """
    # Buat figure
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Buat countplot
    sns.countplot(
        x='has_health_issues',
        data=df,
        palette='husl',
        ax=ax
    )
    
    # Atur judul dan label
    ax.set_title('Distribusi Status Kesehatan', fontsize=14, pad=15)
    ax.set_xlabel('Status Kesehatan (0=Tidak, 1=Ya)', fontsize=12)
    ax.set_ylabel('Jumlah Sampel', fontsize=12)
    
    # Hitung dan simpan proporsi
    proporsi = df['has_health_issues'].value_counts(normalize=True)
    
    # Tambahkan anotasi jumlah di atas setiap bar
    for p in ax.patches:
        ax.annotate(
            f'{p.get_height()}',
            (p.get_x() + p.get_width()/2., p.get_height()),
            ha='center',
            va='center',
            xytext=(0, 10),
            textcoords='offset points',
            fontsize=11
        )
    # Tambahkan grid
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Optimalkan layout
    plt.tight_layout()
    
    # Tampilkan figure dan proporsi
    plt.show()
    print("Proporsi:\n", proporsi)
    
    return fig

def eda2():
    """
    Visualisasi distribusi usia berdasarkan status kesehatan
    """
    # Buat figure
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Buat boxplot
    sns.boxplot(
        x='has_health_issues',
        y='age',
        data=df,
        palette='husl',
        ax=ax,
        showmeans=True,
        meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black"}
    )
    
    # Atur judul dan label
    ax.set_title('Distribusi Usia berdasarkan Status Kesehatan', fontsize=14, pad=15)
    ax.set_xlabel('Memiliki Masalah Kesehatan', fontsize=12)
    ax.set_ylabel('Usia', fontsize=12)
    
    # Format x-axis labels
    ax.set_xticklabels(['Tidak', 'Ya'])
    
    # Tambahkan grid
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Optimalkan layout
    plt.tight_layout()
    
    return fig

def eda3():
    # def eda3(df, figsize=(10, 6), palette='husl', title=None):
    # Buat figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Buat KDE plot
    sns.kdeplot(
        data=df,
        x='annual_income_usd',
        hue='has_health_issues',
        fill=True,
        common_norm=False,
        alpha=0.5,
        palette='husl',
        ax=ax
    )
    
    # Atur judul dan label
    plot_title = 'Distribusi Pendapatan Tahunan berdasarkan Status Kesehatan'
    ax.set_title(plot_title, fontsize=14, pad=15)
    ax.set_xlabel('Pendapatan Tahunan (USD)', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    
    # Format legenda
    ax.legend(
        title='Memiliki Masalah Kesehatan',
        labels=['Tidak', 'Ya'],
        frameon=True,
        framealpha=0.8
    )
    
    # Tambahkan grid
    ax.grid(axis='both', linestyle='--', alpha=0.3)
    
    # Optimalkan layout
    plt.tight_layout()
    
    return fig

def eda4():
    # Buat figure dengan 2 subplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Plot 1: Merokok per hari
    sns.boxplot(
        x='has_health_issues',
        y='smokes_per_day',
        data=df,
        palette='husl',
        ax=ax1,
        showmeans=True,
        meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black"}
    )
    ax1.set_title('Konsumsi Rokok per Hari berdasarkan Status Kesehatan', fontsize=14, pad=15)
    ax1.set_xlabel('Memiliki Masalah Kesehatan', fontsize=12)
    ax1.set_ylabel('Jumlah Rokok per Hari', fontsize=12)
    ax1.set_xticklabels(['Tidak', 'Ya'])
    ax1.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Plot 2: Minum per minggu
    sns.boxplot(
        x='has_health_issues',
        y='drinks_per_week',
        data=df,
        palette='husl',
        ax=ax2,
        showmeans=True,
        meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black"}
    )
    ax2.set_title('Konsumsi Alkohol per Minggu berdasarkan Status Kesehatan', fontsize=14, pad=15)
    ax2.set_xlabel('Memiliki Masalah Kesehatan', fontsize=12)
    ax2.set_ylabel('Jumlah Minuman per Minggu', fontsize=12)
    ax2.set_xticklabels(['Tidak', 'Ya'])
    ax2.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Optimalkan layout
    plt.tight_layout()
    
    return fig

def eda5():
    # Pilih fitur numerik
    num_features = [
        'age', 'annual_income_usd', 'smokes_per_day', 'drinks_per_week',
        'age_started_smoking', 'age_started_drinking',
        'attempts_to_quit_smoking', 'attempts_to_quit_drinking', 
        'sleep_hours', 'bmi'
    ]
    
    # Hitung korelasi
    corr = df[num_features + ['has_health_issues']].corr()
    
    # Buat figure dan axes
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Buat heatmap dengan berbagai pengaturan visual
    heatmap = sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        center=0,
        fmt=".2f",  # Format 2 digit desimal
        linewidths=0.5,
        linecolor='white',
        square=True,
        cbar_kws={"shrink": 0.8},
        ax=ax
    )
    # Atur judul dan font
    ax.set_title(
        'Korelasi Fitur Numerik dengan Health Issues',
        fontsize=14,
        pad=20
    )
    
    # Rotasi label x-axis
    plt.xticks(rotation=45, ha='right')
    
    # Optimalkan layout
    plt.tight_layout()
    
    return fig

def eda6():
    # Hitung proporsi
    gender_rate = df.groupby('gender')['has_health_issues'].mean().reset_index()
    
    # Buat figure
    fig, ax = plt.subplots(figsize=(8, 5))
    # Buat barplot
    barplot = sns.barplot(
        x='gender', 
        y='has_health_issues', 
        data=gender_rate,
        ax=ax,
        palette='pastel',  # Warna yang lebih soft
        edgecolor='black'  # Garis tepi untuk kontras
    )
    # Atur judul dan label
    ax.set_title('Proporsi Health Issues Berdasarkan Gender', fontsize=14, pad=20)
    ax.set_xlabel('Gender', fontsize=12)
    ax.set_ylabel('Proporsi Health Issues', fontsize=12)
    
    # Atur y-axis limit
    ax.set_ylim(0, 1)
    
    # Tambahkan nilai persentase di atas setiap bar
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width()/2.,
            height + 0.02,
            f'{height:.1%}',
            ha='center',
            va='bottom',
            fontsize=12
        )
    # Tambahkan grid untuk kemudahan membaca
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Optimalkan layout
    plt.tight_layout()
    
    return fig

def eda7():
    # Create figure with two subplots
    fig, axes = plt.subplots(2, 1, figsize=(10, 12))
    
    # Plot 1: Countplot
    sns.countplot(
        x='social_support', 
        hue='has_health_issues', 
        data=df, 
        ax=axes[0],
        order=['Weak', 'Moderate', 'Strong']  # Ensure consistent order
    )
    axes[0].set_title('Distribusi Health Issues Berdasarkan Social Support', fontsize=14)
    axes[0].set_xlabel('Tingkat Social Support', fontsize=12)
    axes[0].set_ylabel('Jumlah Sampel', fontsize=12)
    axes[0].legend(title='Health Issues', loc='best')
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Plot 2: Proportion plot
    prop = df.groupby('social_support')['has_health_issues'].mean().reset_index()
    
    sns.barplot(
        x='social_support',
        y='has_health_issues',
        data=prop,
        order=['Weak', 'Moderate', 'Strong'],
        ax=axes[1],
        palette='viridis'
    )
    axes[1].set_title('Proporsi Health Issues per Tingkat Social Support', fontsize=14)
    axes[1].set_xlabel('Tingkat Social Support', fontsize=12)
    axes[1].set_ylabel('Proporsi Health Issues', fontsize=12)
    axes[1].set_ylim(0, 1)
    
    # Menambahkan label persentase di atas setiap bar
    for p in axes[1].patches:
        axes[1].annotate(
            f'{p.get_height():.2%}', 
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center', 
            xytext=(0, 10), 
            textcoords='offset points',
            fontsize=10
        )
    
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Adjust layout
    plt.tight_layout(pad=3.0)
    return fig