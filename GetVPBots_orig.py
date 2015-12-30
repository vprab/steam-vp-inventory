#!/usr/bin/python
__author__ = 'Vishant'
import steam
from termcolor import colored
import os

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

API_KEY = 'D77FC95E768AB539A015918922E63EB8'
steam.api.key.set(API_KEY)

# item_name = "Exalted Frost Avalanche"
# item_parameter = "Shawl and Upgraded Wolf Pup (Locked)"

# item_name = "Virtus Werebear"
# item_parameter = "Tier 3 (Locked)"

# item_name = "Genuine Lieutenant Squawkins"
# item_parameter = "Sailboat Squawkins (Locked)"

# item_name = "Genuine Wyvern Hatchling"
# item_parameter = "Gold (Locked)"

# item_name = "Limbs of Entwined Fate"
# item_parameter = "Skittering Limbs (Locked)"

# item_name = "Almond the Frondillo"
# item_parameter = "Almond the Frondillo Golden Upgrade (Locked)"

# item_name = "Exalted Fractal Horns of Inner Abysm"
# item_parameter = "Reflection's Shade"

# item_name = "Exalted Manifold Paradox"
# item_parameter = "Style 3 (Locked)"

item_dict = {}
# item_dict['Exalted Fractal Horns of Inner Abysm'] = "Reflection's Shade"
item_dict['Fractal Horns of Inner Abysm'] = "Reflection's Shade"
item_dict['Inscribed Fractal Horns of Inner Abysm'] = "Reflection's Shade"
# item_dict['Exalted Frost Avalanche'] = "Shawl and Upgraded Wolf Pup (Locked)"
# item_dict['Exalted Manifold Paradox'] = "Style 3 (Locked)"
# item_dict['Mantle of the Cinder Baron'] = "Style 2 (Locked)"
item_dict['Almond the Frondillo'] = "Almond the Frondillo Golden Upgrade (Locked)"
# item_dict = {"Exalted Fractal Horns of Inner Abysm":"Reflection's Shade", "Exalted Manifold Paradox":"Style 3 (Locked)"}


VPGAME_BOTS = ['76561198113841713', '76561198113916563', '76561198113869089', '76561198113871288', '76561198113895577',
               '76561198113853012', '76561198113841538', '76561198113890905', '76561198113901893', '76561198113865140',
               '76561198113905153', '76561198113875798', '76561198113902498', '76561198113866850', '76561198113895152',
               '76561198113851400', '76561198113840308', '76561198113889846', '76561198113839006', '76561198113876146',
               '76561198113871633', '76561198113853995', '76561198113864826', '76561198113944379', '76561198113882014',
               '76561198113879636', '76561198113866422', '76561198113907695', '76561198113915665', '76561198114292797',
               '76561198114277184', '76561198114281889', '76561198114263433', '76561198114281295', '76561198114239992',
               '76561198114287731', '76561198114252296', '76561198114265693', '76561198114259227', '76561198114317097',
               '76561198114276233', '76561198114288243', '76561198114277194', '76561198114272234', '76561198114278240',
               '76561198114263768', '76561198114272249', '76561198114284405', '76561198119232938', '76561198119197899',
               '76561198119244614', '76561198119187306', '76561198119270383', '76561198119215923', '76561198119221222',
               '76561198119332625', '76561198119326021', '76561198119332621', '76561198119307980', '76561198119350185',
               '76561198119374835', '76561198119354787', '76561198119328419', '76561198119310215', '76561198119328723',
               '76561198119285348', '76561198119315773', '76561198119240848', '76561198119333039', '76561198119326408',
               '76561198119311659', '76561198119376355', '76561198119282517', '76561198119286640', '76561198119347591',
               '76561198119369178', '76561198119290098', '76561198119263588', '76561198119354474', '76561198119312008',
               '76561198119390311', '76561198119302750', '76561198119355657', '76561198119331915', '76561198119348912',
               '76561198119319575', '76561198119377939', '76561198119392059', '76561198119243454', '76561198119286241',
               '76561198119313046', '76561198119314060', '76561198119380991', '76561198119223910', '76561198119289684',
               '76561198119292720', '76561198121385203', '76561198121266280', '76561198121364996', '76561198121319840',
               '76561198121381769', '76561198121403999', '76561198121400165', '76561198121417835', '76561198121324858',
               '76561198121340877', '76561198121395877', '76561198121262330', '76561198121342987', '76561198121329663',
               '76561198121376908', '76561198121275224', '76561198121403879', '76561198121356800', '76561198121329349',
               '76561198121381600', '76561198121383873', '76561198121254616', '76561198121347542', '76561198121331854',
               '76561198121464655', '76561198121278808', '76561198121323802', '76561198121377275', '76561198121392195',
               '76561198121377427', '76561198121348945', '76561198121380302', '76561198121402033', '76561198121401065',
               '76561198121349447', '76561198121375981', '76561198121363921', '76561198121340435', '76561198121429566',
               '76561198121340815', '76561198121337326', '76561198146003603', '76561198146054886', '76561198146042794',
               '76561198145988407', '76561198145962350', '76561198146033556', '76561198148345704', '76561198148281085',
               '76561198148282279', '76561198148292639', '76561198148384592', '76561198148284534', '76561198148394177',
               '76561198148275250', '76561198148297920', '76561198148325758', '76561198148341896', '76561198148249118',
               '76561198148327464', '76561198148297215', '76561198148384727', '76561198148287829', '76561198148350580',
               '76561198148400460', '76561198148299740', '76561198148310487', '76561198148330889', '76561198148355105',
               '76561198148263098', '76561198148383054', '76561198148379294', '76561198148283450', '76561198148316317',
               '76561198148297007', '76561198148258035', '76561198148370791', '76561198148285850', '76561198172533537',
               '76561198148360780', '76561198148292852', '76561198148346625', '76561198148350983', '76561198148314849',
               '76561198148395827', '76561198148402286', '76561198148348663', '76561198148361682', '76561198148363504',
               '76561198148358612', '76561198148365866', '76561198148401901', '76561198148486164', '76561198148517159',
               '76561198148448255', '76561198148441038', '76561198148529703', '76561198148558160', '76561198148507967',
               '76561198149842028', '76561198148451729', '76561198148452655', '76561198148531823', '76561198148466040',
               '76561198148589909', '76561198148563732', '76561198148655101', '76561198148577531', '76561198148555452',
               '76561198148584985', '76561198148589870', '76561198148621344', '76561198148593451', '76561198148649544',
               '76561198148798365', '76561198148704114', '76561198148717938', '76561198148734131', '76561198148756420',
               '76561198148816984', '76561198148803556', '76561198148781944', '76561198148833488', '76561198148785658',
               '76561198148778902', '76561198148843260', '76561198148846311', '76561198148809669', '76561198148734138',
               '76561198148794664', '76561198148852086', '76561198148762308', '76561198148862081', '76561198148798383',
               '76561198148754448', '76561198148810416', '76561198148762840', '76561198148780271', '76561198148813597',
               '76561198157979851', '76561198157967798', '76561198158084171', '76561198158005043', '76561198158115610',
               '76561198157995440', '76561198158090292', '76561198158059353', '76561198158107595', '76561198158072933',
               '76561198158127957', '76561198157947318', '76561198158010736', '76561198158095582', '76561198158059424',
               '76561198158074925', '76561198158128427', '76561198158245181', '76561198158145229', '76561198158120368',
               '76561198158207887', '76561198158191667', '76561198158053618', '76561198158165454', '76561198158195459',
               '76561198158154696', '76561198158147029', '76561198158203292', '76561198158138034', '76561198158088335',
               '76561198158119643', '76561198158184033', '76561198158173412', '76561198158247783', '76561198158159037',
               '76561198158136730', '76561198158189758', '76561198158133409', '76561198158083119', '76561198158078998',
               '76561198158148606', '76561198158127643', '76561198158272286', '76561198158157306', '76561198158331990',
               '76561198158133955', '76561198158206008', '76561198161511418', '76561198161618161', '76561198161737788',
               '76561198161703360', '76561198161639794', '76561198161596334', '76561198161633495', '76561198161654311',
               '76561198161632654', '76561198161641376', '76561198161572130', '76561198161674271', '76561198161575751',
               '76561198161591478', '76561198161598324', '76561198161644176', '76561198161596637', '76561198161541399',
               '76561198161512419', '76561198161597137', '76561198161636015', '76561198161641872', '76561198161759290',
               '76561198161577336', '76561198161694257', '76561198161664239', '76561198161581051', '76561198161519618',
               '76561198161714603', '76561198161622693', '76561198161651733', '76561198161761090', '76561198161577207',
               '76561198161579936', '76561198161720073', '76561198161570962', '76561198161607534', '76561198161579507',
               '76561198161608434', '76561198161590179', '76561198161629996', '76561198161622789', '76561198161693982',
               '76561198161644866', '76561198161642815', '76561198161573338', '76561198161597953', '76561198161631896',
               '76561198161526518', '76561198163181578', '76561198163665406', '76561198163675231', '76561198163789603',
               '76561198163750523', '76561198163773883', '76561198163847990', '76561198163716880', '76561198163616850',
               '76561198163834686', '76561198163712354', '76561198163683740', '76561198163775283', '76561198163721558',
               '76561198163775827', '76561198163660563', '76561198163759776', '76561198163707704', '76561198163680653',
               '76561198163687938', '76561198163714154', '76561198163773657', '76561198163741710', '76561198163774871',
               '76561198163738192', '76561198163643736', '76561198163725693', '76561198163752233', '76561198163714878',
               '76561198163734311', '76561198163706422', '76561198163681520', '76561198163762159', '76561198163752487',
               '76561198163697908', '76561198163666107', '76561198163635944', '76561198163683953', '76561198163726915',
               '76561198163647136', '76561198163699134', '76561198163800308', '76561198163956890', '76561198163747709',
               '76561198163738644', '76561198163784651', '76561198163924077', '76561198163848792', '76561198170882113',
               '76561198170887081', '76561198170910967', '76561198170938463', '76561198170938811', '76561198170907395',
               '76561198170919033', '76561198170930331', '76561198203042864', '76561198203038020', '76561198170909233',
               '76561198170931779', '76561198170968459', '76561198170944843', '76561198170941195', '76561198203013588',
               '76561198170936291', '76561198203041592', '76561198170939859', '76561198170922477', '76561198170940911',
               '76561198170957578', '76561198170934559', '76561198170919873', '76561198170933337', '76561198170927967',
               '76561198170937747', '76561198170980614', '76561198170925877', '76561198170929127', '76561198170931751',
               '76561198170981866', '76561198170941047', '76561198203044368', '76561198170924535', '76561198203058600',
               '76561198170924421', '76561198203044660', '76561198170951158', '76561198203060920', '76561198170930365',
               '76561198170929357', '76561198170952367', '76561198203046632', '76561198170955662', '76561198170955338',
               '76561198170924433', '76561198203052788', '76561198170987806', '76561198170949487', '76561198203039720',
               '76561198170943022', '76561198170932869', '76561198170940395', '76561198170983654', '76561198170946971',
               '76561198170972338', '76561198170943905', '76561198170936977', '76561198170957651', '76561198203040856',
               '76561198203045384', '76561198203054924', '76561198170925773', '76561198203056460', '76561198170941733',
               '76561198170961366', '76561198170926345', '76561198170949878', '76561198203046984', '76561198203061896',
               '76561198172101926', '76561198172100983', '76561198172157575', '76561198172131490', '76561198204223184',
               '76561198172141370', '76561198172116257', '76561198172089709', '76561198204225204', '76561198172134235',
               '76561198172135247', '76561198172123530', '76561198172121846', '76561198172131582', '76561198172135174',
               '76561198172105411', '76561198172143850', '76561198172125386', '76561198172142826', '76561198172154258',
               '76561198204207904', '76561198204206404', '76561198172085001', '76561198172087641', '76561198204208600',
               '76561198204219148', '76561198204216636', '76561198172092349', '76561198172145211', '76561198213580703',
               '76561198213432087', '76561198245746460', '76561198213480897', '76561198245675214', '76561198245606504',
               '76561198213516493', '76561198245699000', '76561198245684514', '76561198245725350', '76561198245668534',
               '76561198213448635', '76561198245684924', '76561198245619484', '76561198213584735', '76561198213546367',
               '76561198245689964', '76561198245663792', '76561198213584519', '76561198213522853', '76561198245721726',
               '76561198245716376', '76561198245694072', '76561198245677660', '76561198213594111', '76561198245710328',
               '76561198245658968', '76561198213544841', '76561198245672116', '76561198213538625', '76561198213584877',
               '76561198245701058', '76561198245695034', '76561198213569669', '76561198213532495', '76561198213533843',
               '76561198245654098', '76561198213468459', '76561198245759536', '76561198245690562', '76561198245703488',
               '76561198245659226', '76561198245760944', '76561198245715312', '76561198245665114', '76561198245684968',
               '76561198213624163', '76561198213594817', '76561198191260491', '76561198245819696', '76561198245873102',
               '76561198245895760', '76561198245867080', '76561198213721481', '76561198245857116', '76561198245852418',
               '76561198213768137', '76561198245884286', '76561198245917648', '76561198213778845', '76561198245873570',
               '76561198245896420', '76561198245888994', '76561198245848344', '76561198213743313', '76561198245859184',
               '76561198213723919', '76561198213734553', '76561198245888678', '76561198245841434', '76561198213652775',
               '76561198213802695', '76561198245869572', '76561198213754749', '76561198213748763', '76561198213804701',
               '76561198245815806', '76561198245888034', '76561198213778029', '76561198213766887', '76561198213751425',
               '76561198245867578', '76561198213768381', '76561198213760541', '76561198213790783', '76561198213775047',
               '76561198213721193', '76561198213667171', '76561198246422242', '76561198246393416', '76561198214338211',
               '76561198246457908', '76561198214291033', '76561198246466878', '76561198246489988', '76561198214358465',
               '76561198246407318', '76561198214258227', '76561198246472166', '76561198214303911', '76561198246430542',
               '76561198214311443', '76561198246450118', '76561198214323659', '76561198214304605', '76561198246474510',
               '76561198246496786', '76561198214346595', '76561198214330831', '76561198214363899', '76561198246506934',
               '76561198214341211', '76561198214283329', '76561198246513054', '76561198246489850', '76561198246489968',
               '76561198214335081', '76561198246451386', '76561198246507354', '76561198246452330', '76561198246480046',
               '76561198246433606', '76561198246501470', '76561198246439898', '76561198246454858', '76561198246419170',
               '76561198214323241', '76561198246449420', '76561198214293863', '76561198246495786', '76561198246508714',
               '76561198214334179', '76561198246432710', '76561198246445742', '76561198214325107', '76561198246485768',
               '76561198246501214', '76561198214418697', '76561198214337955', '76561198214356345', '76561198214371047',
               '76561198246489880', '76561198246461338', '76561198246533838', '76561198246512400', '76561198214417129',
               '76561198214363531', '76561198246558308', '76561198246526014', '76561198251491120', '76561198251367550',
               '76561198251423366', '76561198251426412', '76561198219307007', '76561198251420610', '76561198219308423',
               '76561198251427830', '76561198251413640', '76561198219294255', '76561198251419414', '76561198219289849',
               '76561198251467096', '76561198251528832', '76561198219360601', '76561198251539138', '76561198219505323',
               '76561198251593530', '76561198219431795', '76561198251542670', '76561198251520634', '76561198251544570',
               '76561198251507470', '76561198251533030', '76561198251533384', '76561198219424685', '76561198251543614',
               '76561198251493842', '76561198251652360', '76561198251551474', '76561198251532910', '76561198251623044',
               '76561198219400355', '76561198219442071', '76561198219375659', '76561198251609574', '76561198219473421',
               '76561198219539485', '76561198219595583', '76561198219565015', '76561198219594331', '76561198251741506',
               '76561198251736062', '76561198219532355', '76561198219607577', '76561198219541609', '76561198219527639',
               '76561198219541005', '76561198251684088', '76561198219653885', '76561198251675604', '76561198251677610',
               '76561198219544073', '76561198219499203', '76561198251742918', '76561198251770370', '76561198251749986',
               '76561198251609486', '76561198251710082', '76561198251720038', '76561198219621417', '76561198219608893',
               '76561198251756072']

GOOD_BOTS = []
ERROR_BOTS = {}
ERROR_COUNT = 0

while VPGAME_BOTS != []:
    for bot in VPGAME_BOTS:
        try:
            inventory_context = steam.sim.inventory_context(bot)
            inventory = steam.sim.inventory(inventory_context.get(570), bot)

            for item_name in item_dict:
                good = False
                item_parameter = item_dict[item_name]

                arcanas = [item for item in inventory if item.name == item_name]

                if len(arcanas) is 1:
                    for item in arcanas:
                        if all([item_parameter not in att.description for att in item.attributes]):
                            good = True
                            GOOD_BOTS.append(bot)

                if good:
                    print colored("%s SUCCESS %s" % (bot, item_name), 'green')
                    notify(title = 'VP Bot', subtitle = 'Success!', message = '%s : %s' % (item_name, bot))
                    # os.system('say "success!"')
                # else:
                #     print colored("%s FAILURE" % bot, 'red')

            VPGAME_BOTS.remove(bot)
        except:
            if bot not in ERROR_BOTS:
                ERROR_BOTS[bot] = 1
            else:
                ERROR_BOTS[bot] += 1

            if ERROR_BOTS[bot] is 5:
                ERROR_COUNT += 1
                VPGAME_BOTS.remove(bot)

            # print colored("%s ERROR" % bot, 'yellow')

print GOOD_BOTS
print ERROR_BOTS
print ERROR_COUNT
