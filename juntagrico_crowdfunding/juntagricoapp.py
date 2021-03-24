from juntagrico.util import addons

import juntagrico_crowdfunding

addons.config.register_user_menu('cf/menu/crowdfunding_user_menu.html')
addons.config.register_version(juntagrico_crowdfunding.name, juntagrico_crowdfunding.version)
