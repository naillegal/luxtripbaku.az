from django import template

register = template.Library()


@register.filter
def country_flag(value):
    country_mapping = {
        '+': '',  # Type your own
        '+994': 'az',  # Azerbaijan
        '+968': 'om',  # Oman
        '+973': 'bh',  # Bahrain
        '+965': 'kw',  # Kuwait
        '+974': 'qa',  # Qatar
        '+966': 'sa',  # Saudi Arabia
        '+967': 'ye',  # Yemen
        '+1': 'us',  # United States
        '+44': 'gb',  # United Kingdom
        '+90': 'tr',  # Turkey
        '+33': 'fr',  # France
        '+49': 'de',  # Germany
        '+61': 'au',  # Australia
        '+81': 'jp',  # Japan
        '+86': 'cn',  # China
        '+91': 'in',  # India
        '+55': 'br',  # Brazil
        '+7': 'ru',  # Russia
        '+34': 'es',  # Spain
        '+39': 'it',  # Italy
        '+52': 'mx',  # Mexico
        '+82': 'kr',  # South Korea
        '+27': 'za',  # South Africa
        '+46': 'se',  # Sweden
        '+31': 'nl',  # Netherlands
        '+45': 'dk',  # Denmark
        '+47': 'no',  # Norway
        '+48': 'pl',  # Poland
        '+32': 'be',  # Belgium
        '+420': 'cz',  # Czech Republic
        '+41': 'ch',  # Switzerland
        '+234': 'ng',  # Nigeria
        '+351': 'pt',  # Portugal
        '+66': 'th',  # Thailand
        '+971': 'ae',  # United Arab Emirates
        '+92': 'pk',  # Pakistan
        '+63': 'ph',  # Philippines
        '+60': 'my',  # Malaysia
        '+353': 'ie',  # Ireland
        '+62': 'id',  # Indonesia
        '+64': 'nz',  # New Zealand
        '+998': 'uz',  # Uzbekistan
    }
    return country_mapping.get(value, 'az')
