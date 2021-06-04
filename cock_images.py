import pathlib


def cocktail_image():
    # 이미지의 저장경로를 불러옴.
    image_path = str(pathlib.Path(__file__).parent.absolute())
    image_path = image_path.replace("\\", "/", 10)

    transparent = ['transparent', image_path + '/images/transparent_image2.png']
    kir = ['kir', image_path + '/images/kir.png']
    negroni = ['negroni', image_path + '/images/negroni.png']
    old_fashioned = ['old_fashioned', image_path + '/images/old_fashioned.png']
    rusty_nail = ['rusty_nail', image_path + '/images/rusty_nail.png']
    black_russian = ['black_russian', image_path + '/images/black_russian.png']
    moscow_mule = ['moscow_mule', image_path + '/images/moscow_mule.png']
    bloody_mary = ['bloody_mary', image_path + '/images/bloody_mary.png']
    seabreeze = ['seabreeze', image_path + '/images/seabreeze.png']
    cuba_libre = ['cuba_libre',image_path + '/images/cuba_libre.png']
    long_island_ice_tea = ['long_island_ice_tea', image_path + '/images/long_island_iced_tea.png']
    harvey_wallbanger = ['harvey_wallbanger', image_path + '/images/harvey_wallbanger.png']
    tequila_sunrise = ['tequila_sunrise', image_path + '/images/tequila_sunrise.png']
    mai_tai = ['mai_tai', image_path + '/images/mai_tai.png']
    blue_hawaiian = ['blue_hawaiian', image_path + '/images/blue_hawaiian.png']
    pina_colada = ['pina_colada', image_path + '/images/pina_colada.png']
    b_52 = ['b_52', image_path + '/images/b_52.png']
    pousse_cafe = ['pousse_cafe', image_path + '/images/pousse_cafe.png']
    manhattan = ['manhattan', image_path + '/images/manhattan.png']
    dry_martini = ['dry_martini', image_path + '/images/dry_martini.png']
    gochang = ['gochang', image_path + '/images/gochang.png']
    sloe_gin_fizz = ['sloe_gin_fizz', image_path + '/images/sloe_gin_fizz.png']
    whisky_sour = ['whisky_sour', image_path + '/images/whisky_sour.png']
    singapore_sling = ['singapore_sling', image_path + '/images/singapore_sling.png']
    honeymoon = ['honeymoon', image_path + '/images/honeymoon.png']
    sidecar = ['sidecar', image_path + '/images/sidecar.png']
    brandy_alexander = ['brandy_alexander', image_path + 'brandy_alexander/images/.png']
    newyork = ['newyork', image_path + '/images/newyork.png']
    margarita = ['margarita', image_path + '/images/margarita.png']
    apple_martini = ['apple_martini', image_path + '/images/apple_martini.png']
    kiss_of_fire = ['kiss_of_fire', image_path + '/images/kiss_of_fire.png']
    cosmopolitan = ['cosmopolitan', image_path + '/images/cosmopolitan.png']
    bacardi = ['bacardi', image_path + '/images/bacardi.png']
    daiquiri = ['daiquiri', image_path + '/images/daiquiri.png']
    june_bug = ['june_bug', image_path + '/images/june_bug.png']
    grasshopper = ['grasshopper', image_path + '/images/grasshopper.png']
    apricot = ['apricot', image_path + '/images/apricot.png']
    geumsan = ['geumsan', image_path + '/images/geumsan.png']
    jindo = ['jindo', image_path + '/images/jindo.png']
    puppy_love = ['puppy_love', image_path + '/images/puppy_love.png']
    healing = ['healing', image_path + '/images/healing.png']

    all_images = [transparent, kir, negroni, old_fashioned, rusty_nail, black_russian, moscow_mule, bloody_mary,
                  seabreeze, cuba_libre, long_island_ice_tea, harvey_wallbanger, tequila_sunrise, mai_tai,
                  blue_hawaiian, pina_colada, b_52, pousse_cafe, manhattan, dry_martini, gochang, sloe_gin_fizz,
                  whisky_sour, singapore_sling, honeymoon, sidecar, brandy_alexander, newyork, margarita, apple_martini,
                  kiss_of_fire, cosmopolitan, bacardi, daiquiri, june_bug, grasshopper, apricot, geumsan, jindo,
                  puppy_love, healing]

    return all_images


cocktail_image()