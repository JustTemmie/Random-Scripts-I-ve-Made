import requests
import random
import subprocess
import os
import time

#path = './beavers/' 
#try: 
#    os.mkdir(path) 
#except OSError as error: 
#    print(error)  

print("a")
if __name__ == "__main__":

    
    beavers = [
        "https://upload.wikimedia.org/wikipedia/commons/6/6b/American_Beaver.jpg",
        "https://ichef.bbci.co.uk/news/976/cpsprodpb/0344/production/_115563800_gettyimages-978603162.jpg",
        "https://www.nina.no/portals/nina/Bilder%20og%20dokumenter/Beaver-eating-apple-Photo-Ian-Sargent_1200.jpg",
        "https://www1.nyc.gov/assets/wildlifenyc/images/content/pages/beaver-with-stick_istock-resized.jpg",
        "https://static.scientificamerican.com/sciam/cache/file/B365F8DD-C0BE-49C6-9BB33B41EFC6C9A6_source.png?w=590&h=800&010A70C5-49C5-42B0-AEA06C783E5FC35A",
        "https://static01.nyt.com/images/2017/12/21/climate/21CLI-BEAVERS/merlin_131321107_e96f4279-5637-404a-b092-261b19d09bcd-superJumbo.jpg?quality=75&auto=webp",
        "https://i.guim.co.uk/img/media/a7c2294ae580cfe6ef358573a95e5c0637cdc7f5/0_160_4797_2878/master/4797.jpg?width=1020&quality=85&auto=format&fit=max&s=89a240d75ddc37b4ef1804ee1ef41c99",
        "https://rewildingbritain.imgix.net/images/beaver-uk-river.jpg?crop=focalpoint&domain=rewildingbritain.imgix.net&fit=crop&fm=webp&fp-x=0.5&fp-y=0.5&h=1125&ixlib=php-3.3.1&q=82&usm=20&w=2000",
        "https://www.ntu.ac.uk/__data/assets/image/0025/1426363/beaver-Cornwall-WT-cpt-Nick-Upton-for-web.jpg",
        "https://www.sierraclub.org/sites/www.sierraclub.org/files/styles/flexslider_full/public/sierra/articles/big/SIERRA-iStock-842493890-WB.jpg?itok=4HYWDi7e",
        "https://www.carolinacountry.com/media/zoo/images/beaver-pair-USFWS_31a9f0b3cb33bde8e3b9b5a7e00644bb.jpg",
        "https://www.washingtonpost.com/news/animalia/wp-content/uploads/sites/56/2018/08/beaver1.jpg",
        "https://www.preventionweb.net/sites/default/files/styles/landscape_16_9/public/2022-01/Image-Beaver.jpg?h=2cf907fb&itok=KPPngPLI",
        "https://www.sierraclub.org/sites/www.sierraclub.org/files/styles/flexslider_full/public/sierra/articles/big/SIERRA-iStock-1143334124-WB.jpg?itok=ElWkW8PW",
        "https://i.guim.co.uk/img/media/575257f27848cb1f278b64387c7f32e27df70f94/0_110_3205_1924/master/3205.jpg?width=700&quality=85&auto=format&fit=max&s=9c3230aadb0e6c27cc574d927c328f9f",
        "https://www.gardeningknowhow.com/wp-content/uploads/2020/12/begging-beaver-400x300.jpg",
        "https://a-z-animals.com/media/2021/10/What-Do-Beavers-Eat-1024x576.jpg",
        "https://a-z-animals.com/media/2021/10/shutterstock_1068631397.jpg",
        "https://www.nps.gov/voya/learn/nature/images/VOYA_web_Wildlife_BeaverLodge.jpg?maxwidth=1200&maxheight=1200&autorotate=false",
        "https://www.nps.gov/voya/learn/nature/images/VOYA_web_beaver_chew_tree.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "https://gray-kcbd-prod.cdn.arcpublishing.com/resizer/-MSeub1FVJIa8k36g0TRtanmNqw=/1200x675/smart/filters:quality(85)/cloudfront-us-east-1.images.arcpublishing.com/gray/RG5JRSEEXJDGRGZ6ZBSYGDUGPY.jpg",
        "https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Ftimes%2Fprod%2Fweb%2Fbin%2F64feeeb4-4b58-11ea-b112-75acb94b3417.jpg?crop=3495%2C1966%2C508%2C672&resize=1200"
        "https://www.akademika.no/sites/default/files/styles/product_zoom/public/product_images/978/0/1/9/8/8/3/9780198835042.jpg?itok=wOU79lw-",    
    ]


    file_paths = [
        "./Downloads/beav",
        "./Downloads/beaver",
        "./Downloads/beavy",
        
        "./Documents/beav",
        "./Documents/beaver",
        "./Documents/beavy",
        
        "./Pictures/beav",
        "./Pictures/beaver",
        "./Pictures/beavy",
        
        "./beav",
        "./beaver",
        "./beavy",
        
        "./beavers/beav",
        "./beavers/beaver",
        "./beavers/beavy",
    ]

    while True:
        time.sleep(random.randint(7200,21600))
        ran_num = random.randint(0, 99999)

        path = file_paths[random.randrange(0, len(file_paths))] + str(ran_num) + ".png"


        url = beavers[random.randrange(0, len(beavers))]
        r = requests.get(url, allow_redirects=True)


        open(path ,"wb").write(r.content)

        if random.randrange(0, 60) == 4:
            subprocess.call("eog " + path, shell=True)
