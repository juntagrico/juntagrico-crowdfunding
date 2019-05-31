from django.template.loader import get_template

from juntagrico.config import Config
from juntagrico.mailer import send_mail, get_server

from juntagrico_crowdfunding.config import CrowdfundingConfig

'''
Server generated Emails
'''

def send_fund_confirmation_mail(fund, password=None):

    plaintext = get_template(CrowdfundingConfig.emails('fund_confirmation_mail'))

    d = {
        'fund': fund,
        'password': password,
        'serverurl': get_server()
    }

    content = plaintext.render(d)
    send_mail(Config.organisation_name() + ' - Beitragsbestätigung', content, Config.info_email(), [fund.funder.email])
