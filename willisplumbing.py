import os
import io, os
import chardet
import codecs
import html
import re
from bs4 import BeautifulSoup
import requests
import random
import shutil

home_page_template= '''
        <div class="col-m-2" id="aloomafotter1">
            <div id="aloomafotter2"><a href="aloomaidstaturl" id="aloomafotter">aloomaidstate</a></div>
        </div>
'''
metatileanddescripttion= '''
    <script>
        // Define the meta title string
        let metaTitles = "{{aloomaidtitle}}";

        // Define the meta description string
        let metaDescriptions = "{{aloomaiddescription}}";

        // Function to randomly pick from an array
        function getRandomItem(text) {
            let items = text.split("@@@").map(item => item.trim());
            return items[Math.floor(Math.random() * items.length)];
        }

        // Set the document title
        document.title = getRandomItem(metaTitles);

        // Set the meta description dynamically
        let metaDescriptionTag = document.querySelector('meta[name="description"]');
        if (metaDescriptionTag) {
            metaDescriptionTag.setAttribute("content", getRandomItem(metaDescriptions));
        } else {
            let newMetaTag = document.createElement('meta');
            newMetaTag.name = "description";
            newMetaTag.content = getRandomItem(metaDescriptions);
            document.head.appendChild(newMetaTag);
        }
    </script>
</head>
'''

processing_handler= '''<div id="output"></div>
    <script>
        
        function getContents(selectedContents, splitInfo) {
            let [header, paragraph] = selectedContents.split(splitInfo);
            header = header.replace(/<br>/g, '');
            paragraph = paragraph.replace(/<br><br>/g, '<br>');

            let secondPart = '';
            if (paragraph.includes('<list>')) {
                let [partParagraph, listParagraph] = paragraph.split('<list>');
                let listItems = listParagraph.replace(/<br>/g, '').replace(/\\n/g, '').split('^^');
                let appendAllList = listItems.map(item => `<li>${item}</li>`).join('');
                secondPart = `<ul>${appendAllList}</ul>`;
                return [header, partParagraph, secondPart];
            }
            return [header, paragraph, secondPart];
        }

        function cleanText(htmlContent) {
            let result = htmlContent;
            let regex = /{([^{}()]+)}/g;
            result = result.replace(regex, (match, p1) => {
                if (p1.includes('|')) {
                    let options = p1.split('|');
                    return options[Math.floor(Math.random() * options.length)];
                }
                return p1;
            });
            return result.replace(/{|}/g, '');
        }

        function handleTemplate(option1, option2) {
            return Math.random() > 0.5 ? option1 : option2;
        }

        function generateContentsBody(phoneNumber, longForm, shortForm, imageList, data, siteName) {
            data = data.replace(/&amp;/g, 'and').replace(/\\n/g, '<br>').replace(/<br><br><br>/g, '<br>').trim();
            data = cleanText(data);
            let allReformattedBody = '';
            let usedImage = [];
            let sanitizedPhone = phoneNumber.replace(/\s|\(|\)|-/g, '');
            let phoneNumberUrl = `tel:${sanitizedPhone}`;
            let allData = data.split('$$');

            let myNini = 0;
            allData.forEach(selectedContents => {
                selectedContents = selectedContents.trim().replace(/\\n/g, '');
                let singleTemplateChecker = '';
                let replace_long_form= `<div class="col-m-6 col-l-6">
                                    aloomalongform
                                </div>`;
                let replace_short_form= `<div class="col-m-4 col-l-4">
                                        aloomashortform
                                    </div>`;
                
                if (selectedContents.includes('%%')) {
                    let multipleChecker = selectedContents.split('%%').length;
                    
                    if (selectedContents.includes('<review>')) {
                        singleTemplateChecker = '<template9>';
                    }else if (selectedContents.includes('<faq>')) {
                        singleTemplateChecker = '<template10>';
                    } else if (multipleChecker === 2) {
                        singleTemplateChecker = '<template7>';
                    } else if (multipleChecker === 3) {
                        singleTemplateChecker = '<template5>';
                    }
                } else {
                    if (selectedContents.includes('<contact>')) {
                        singleTemplateChecker = '<template8>';
                    }  else {
                        if (myNini === 0) {
                            singleTemplateChecker = handleTemplate('<template1>', '<template4>');
                        } else if (myNini === 2) {
                            singleTemplateChecker = handleTemplate('<template2>', '<template3>');
                        } else {
                            singleTemplateChecker = '<template6>';
                        }
                        myNini++;
                    }
                }
                
                if (singleTemplateChecker === '<template1>' ||
                    singleTemplateChecker === '<template2>' ||
                    singleTemplateChecker === '<template3>' ||
                    singleTemplateChecker === '<template4>'
                ) {
                    let [header, mainParagraph, secondPart] = getContents(selectedContents, '<h2>');
                    if (singleTemplateChecker === '<template1>'){
                        let templateData1 = `<!-- Template 1.1 Start -->
                        <br><br>
                        <div class="containeralooma">
                            <section class="boxalooma">
                            <div class="row">
                                <div class="col-m-6 col-l-6">
                                    <h2 class="template1 h2alooma">aloomaidheader</h2>
                                    <p class="template1 palooma">aloomaidparagraph</p>
                                    aloomalistdata
                                    <div class="callalooma"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                </div>
                                <div class="col-m-6 col-l-6">
                                    aloomalongform
                                </div>

                            </div>
                            </section>
                        </div>

                        <!-- Template 1.1 End -->`;
                        templateData = templateData1;
                    }
                    else if (singleTemplateChecker === '<template2>') {
                        let templateData2 = `<!-- Template 2 Start -->
                        <br><br><br><br>
                        <div class="containeralooma" id="ourservices">
                            <section class="boxalooma">
                            <div class="row">
                                <h2 class="template2 mx-auto">aloomaidheader </h2>
                                <p class="template2 palooma mx-auto">aloomaidparagraph
                                </p>
                                <div class="col-m-8 col-l-8">
                                    aloomalistdata
                                    <div class="callalooma"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                </div>
                                <div class="col-m-4 col-l-4">
                                        aloomashortform
                                    </div>
                                
                            </div>
                            </section>  
                        </div>

                        <!-- Template 2 End -->`;
                        templateData = templateData2;
                    }
                    else if (singleTemplateChecker === '<template3>') {
                        let templateData3 = `<!-- Template 3 Start -->
                        <br><br><br><br>
                        <div class="containeralooma">
                            <section class="boxalooma">
                                <div class="row">
                                    <div class="col-m-4 col-l-4">
                                        aloomashortform
                                    </div>
                                    <div class="col-m-8 col-l-8">
                                        <h2 class="h2alooma template3">aloomaidheader</h2>
                                        <p class="template3 palooma">aloomaidparagraph
                                        </p>
                                aloomalistdata
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-12">
                                
                                        <div class="callalooma"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                    </div>
                                </div>
                            </section>
                        </div>


                        <!-- Template 3 End -->`;
                        templateData = templateData3;
                    }
                    else if (singleTemplateChecker === '<template4>') {
                        let templateData4 = `<!-- Template 4 Start -->
                        <br><br><br><br>
                        <div class="containeralooma">
                            <section class="boxalooma">
                                <div class="row">
                                    <div class="col-m-6 col-l-6">
                                        <h2 class="template4 h2alooma">aloomaidheader</h2>
                                        <p class="template4 palooma">aloomaidparagraph
                                        </p>
                                        aloomalistdata
                                        <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                        
                                    </div>
                                    <div class="col-m-6 col-l-6">
                                    aloomalongform
                                </div>
                                </div>
                        
                                
                            </section>
                        </div>

                        <!-- Template 4 End -->`;
                        templateData = templateData4;
                    }
                    if (longForm.length > 3) {
                        templateData = templateData.replace(/aloomaidheader/g, header)
                            .replace(/aloomaidparagraph/g, mainParagraph)
                            .replace(/aloomalistdata/g, secondPart)
                            .replace(/aloomalongform/g, longForm)
                            .replace(/aloomashortform/g, shortForm)
                            .replace(/aloomaidphonenumberful/g, phoneNumber)
                            .replace(/aloomaidphonenumberurl/g, phoneNumberUrl);
                    } else {
                        templateData = templateData.replace(/aloomaidheader/g, header)
                            .replace(/aloomaidparagraph/g, mainParagraph)
                            .replace(/aloomalistdata/g, secondPart)
                            .replace(replace_long_form, '')
                            .replace(replace_short_form, '')
                            .replace(/col-m-6 col-l-6/g, '')
                            .replace(/aloomaidphonenumberful/g, phoneNumber)
                            .replace(/aloomaidphonenumberurl/g, phoneNumberUrl);
                    }
                    allReformattedBody += templateData;
                }
                else if (singleTemplateChecker === '<template5>') {
                    
                    let templateData = `<!-- Template 5 Start -->
                        <br><br><br><br>
                        <div class="containeralooma" id="About">
                            <section class="boxalooma">
                            <div class="row">
                                <div class="col-m-4 col-l-4">
                                    <h2 class="template4 h2alooma">aloomaidheader</h2>
                                    <p class="template4 palooma">aloomaidparagraph
                                    </p>
                                    aloomalistdata
                                    <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                </div>
                                <div class="col-m-4 col-l-4">
                                    <h2 class="template4 h2alooma">aloomaidheader</h2>
                                    <p class="template4 palooma">
                                    aloomaidparagraph
                                    </p>
                                    aloomalistdata
                                    <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                </div>
                                <div class="col-m-4 col-l-4">
                                    <h2 class="template4 h2alooma">aloomaidheader</h2>
                                    <p class="template4 palooma">aloomaidparagraph
                                    </p>
                                    aloomalistdata
                                    <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                </div>
                            </div>
                            </section>
                        </div>

                        <!-- Template 5 End -->`;
                    let allDataSplit = selectedContents.split('%%');
                    
                    allDataSplit.forEach(dataSplit => {
                        let [header, mainParagraph, secondPart] = getContents(dataSplit, '<h2>');
                        templateData = templateData
                            .replace(/aloomaidheader/, header)
                            .replace(/aloomaidparagraph/, mainParagraph)
                            .replace(/aloomalistdata/, secondPart)
                            .replace(/aloomalongform/, longForm)
                            .replace(/aloomashortform/, shortForm)
                            .replace(/aloomaidphonenumberful/, phoneNumber)
                            .replace(/aloomaidphonenumberurl/, phoneNumberUrl);
                    });
                    allReformattedBody += templateData;
                }
                else if (singleTemplateChecker === '<template6>') {
                    let [header, mainParagraph, secondPart] = getContents(selectedContents, '<h2>');
                    let templateData = `<!-- Template 6 Start -->
                        <br><br><br><br>
                        <div class="containeralooma">
                            <section class="boxalooma">
                                <div class="row">
                                    <div class="col-m-8 col-l-8">
                                        <h2 class="template4 h2alooma">aloomaidheader</h2>
                                        <p class="template4 palooma">aloomaidparagraph</p>
                                        aloomalistdata
                                        <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                    </div>
                                    <div class="col-m-4 col-l-4">
                                        <img style="width: 100%" class="aloomacssidimage" src="aloomaidpickimage" alt="aloomaidalttitle">
                                        <br>
                                    </div>
                                </div>
                            </section>
                        </div>

                        <!-- Template 6 End -->`;
                    let counter = 0;
                    let pickImage;
                    do {
                        pickImage = imageList[Math.floor(Math.random() * imageList.length)];
                        counter++;
                    } while (usedImage.includes(pickImage) && counter < 20);
                    usedImage.push(pickImage);
                    let altText = pickImage.split('.')[0];
                    
                    templateData = templateData.replace('aloomaidheader', header)
                        .replace('aloomaidparagraph', mainParagraph)
                        .replace('aloomalistdata', secondPart)
                        .replace('aloomalongform', longForm)
                        .replace('aloomashortform', shortForm)
                        .replace('aloomaidphonenumberful', phoneNumber)
                        .replace('aloomaidphonenumberurl', phoneNumberUrl)
                        .replace('aloomaidpickimage', pickImage)
                        .replace('aloomaidalttitle', altText);
                    allReformattedBody += templateData;
                }
                else if (singleTemplateChecker === '<template7>'){
                    let counter = 0, pickImage, pickImage1;
                    while (counter < 20) {
                        counter++;
                        pickImage = imageList[Math.floor(Math.random() * imageList.length)];
                        if (!usedImage.includes(pickImage)) break;
                    }

                    usedImage.push(pickImage);

                    let counter1 = 0;
                    while (counter1 < 20) {
                        counter1++;
                        pickImage1 = imageList[Math.floor(Math.random() * imageList.length)];
                        if (!usedImage.includes(pickImage1)) break;
                    }

                    let altText = pickImage.split('.')[0];
                    let altText1 = pickImage1.split('.')[0];

                    let templateData = `<!-- template 7 -- two subtopic with a list and image-->
                        <br><br><br><br>
                        <div class="containeralooma">
                            <section class="boxalooma">
                            <div class="row">
                                <div class="col-m-6 col-l-6">
                                    <h2 class="template4 h2alooma">aloomaidheader</h2>
                                    <p class="template4 palooma">aloomaidparagraph
                                    </p>
                                    aloomalistdata
                                    <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                    <br><br>
                                    <img class="aloomacssidimage" src="aloomaidpickimage" alt="aloomaidalttitle">
                                </div>
                                <div class="col-m-6 col-l-6">
                                    <img class="aloomacssidimage" src="aloomaidpickimage" alt="aloomaidalttitle">
                                    <br><br>
                                    <h2 class="template4 h2alooma">aloomaidheader</h2>
                                    <p class="template4 palooma">aloomaidparagraph</p>
                                    aloomalistdata
                                    <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                </div>
                            </div>
                            </section>
                        </div>`;

                    let allDataSplit = selectedContents.split("%%");
                    
                    allDataSplit.forEach(data => {
                        let [ header, mainParagraph, secondPart ] = getContents(data, "<h2>");
                        
                        templateData = templateData
                            .replace("aloomaidheader", header)
                            .replace("aloomaidparagraph", mainParagraph)
                            .replace("aloomalistdata", secondPart)
                            .replace("aloomalongform", longForm)
                            .replace("aloomashortform", shortForm)
                            .replace("aloomaidphonenumberful", phoneNumber)
                            .replace("aloomaidphonenumberurl", phoneNumberUrl)
                            .replace("aloomaidpickimage", pickImage)
                            .replace("aloomaidpickimage", pickImage1)
                            .replace("aloomaidalttitle", altText)
                            .replace("aloomaidalttitle", altText1);
                    });

                    allReformattedBody += templateData;
                    usedImage.push(pickImage1);
                }
                else if (singleTemplateChecker === "<template8>") {
                    // Template 8: Contact template with 1 subtopic
                    let [ header, mainParagraph, secondPart ] = getContents(selectedContents, "<h2>");
                    let templateData = `<br><br><br><br>
                        <div class="containeralooma" id="contact">
                            <section class="boxalooma">
                            <div class="row">
                                <div class="col-12">
                                    <h2 class="template4 h2alooma">aloomaidheader</h2>
                                    <p class="template4 palooma">aloomaidparagraph
                                    </p>
                                    <div class="callalooma mx-auto"><a href="aloomaidphonenumberurl">Click Here To Call Us aloomaidphonenumberful</a></div>
                                </div>
                            </div>
                            </section>
                        </div>
                    `;

                    templateData = templateData
                        .replace("aloomaidheader", header)
                        .replace("aloomaidparagraph", mainParagraph)
                        .replace("aloomalistdata", secondPart)
                        .replace("aloomalongform", longForm)
                        .replace("aloomashortform", shortForm)
                        .replace("aloomaidphonenumberful", phoneNumber)
                        .replace("aloomaidphonenumberurl", phoneNumberUrl)
                        .replace("<contact>", "");

                    allReformattedBody += templateData;
                } 
                else if (singleTemplateChecker === "<template9>") {
                    // Template 9: Reviews
                    let allCommentsData = "";
                    let allDataSplit = selectedContents.split("%%");
                    let commentsTemplate= `<br><br><br><br>
                    <div class="col-m-4">
                        <i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i>
                        <p class="template4 palooma">aloomaidcomments</p>
                        <label for="" style="float: right;">aloomaidcommenname</label>
                    </div>`;
                    allDataSplit.forEach(data => {
                        
                        let [comments, customerName, secondPart ] = getContents(data, "<h2>");
                        allCommentsData += commentsTemplate
                            .replace("aloomaidcomments", comments)
                            .replace("aloomaidcommenname", customerName);
                    });

                    let templateData = `<!-- Reviews  -->
                    <br><br><br><br>
                    <div class="containeralooma" id="review">
                        <section class="boxalooma" style="text-align: center;">
                        <h2 class="heading-with-line template4 h2alooma">Customer Reviews</h2>
                        <div class="row">
                            aloomaidallcomments
                        </div>
                        </section>
                    </div>`;

                    templateData = templateData
                        .replace("aloomaidallcomments", allCommentsData)
                        .replace("<review>", "");

                    allReformattedBody += templateData;
                }
                else if (singleTemplateChecker === "<template10>") {
                    // Template 9: Faq
                    let allCommentsData = "";
                    let allDataSplit = selectedContents.split("%%");
                    let commentsTemplate= `<h4 class="template4 palooma">aloomaidcomments</h4>
                    <p>aloomaidcommenname</p>
                    `;
                    allDataSplit.forEach(data => {
                        
                        let [comments, customerName, secondPart ] = getContents(data, "<h2>");
                        allCommentsData += commentsTemplate
                            .replace("aloomaidcomments", comments)
                            .replace("aloomaidcommenname", customerName);
                    });

                    let templateData = `<br><br><br><br>
                    <div class="containeralooma" id="contact">
                        <section class="boxalooma">
                        <div class="row">
                            <div class="col-12">
                                <h2 class="template4 h2alooma" style="margin-left: 400px;">Frequently Asked Questions in #State</h2>
                                aloomaidallcomments
                                
                            </div>
                        </div>
                        </section>
                    </div>`;

                    templateData = templateData
                        .replace("aloomaidallcomments", allCommentsData)
                        .replace("<faq>", "");

                    allReformattedBody += templateData;
                }
                
            });
            

            document.getElementById("output").innerHTML = allReformattedBody;
        }

        // Example usage
        document.addEventListener("DOMContentLoaded", function() {
            let sampleData = `aloomaspintaxcontentsid`;
            let dataList = sampleData.includes('@@@') 
                ? sampleData.split('@@@').map(item => item.trim()) 
                : [sampleData.trim()];

            // Pick one at random
            let selectedData = dataList[Math.floor(Math.random() * dataList.length)];
            generateContentsBody(`aloomaphonenumberid`, `aloomalongformid`, `aloomashortformid`, aloomalistofimagesid, selectedData, `aloomasitenameid`);
        });

    </script>
'''
county_remove= '''    <br><br><br><br>
    <div class="containeralooma" style="background-color: transparent;">
        <section class="boxalooma" style="text-align: center;">
        <h2 class="heading-with-line template4 h2alooma">Counties In #State</h2>
        <div class="row">
            aloomaidstatecounty
        </div>
        </section>
    </div>
'''

home_page_template1= '''
        <div class="row">
            <div class="col-6 col-s-6 col-m-6 col-l-6" style="border: 2px solid black; text-align:center; background-color: white;"><a href="aloomaidcityurl"><strong>aloomaidcityname</strong></a></div>
            <div class="col-6 col-s-6 col-m-6 col-l-6" style="border: 2px solid black; text-align:center; background-color: white;"><strong>aloomaidzipcode</strong></div>
            
        </div>
'''
def random_homepage_webpage(confirm_home_pages):
    return open(confirm_home_pages, "r", encoding="utf-8-sig").read()

def short_code_state(state_repl):
    search_categories = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        short_code = credential[2].replace('ï»¿', '').upper()
        state_repl1= credential[3].replace('ï»¿', '').title()
        try:
            if state_repl.lower() == state_repl1.lower():
                break
        except:
            break
    return short_code

def home_page_footer(population_limit, rootpath):
    template_data_2 = open("static/aloomaspecial/home_page.txt", "r", encoding="utf-8-sig").read()
    data_plus_plus= open("static/aloomaspecial/content/state.txt", "r", encoding="utf-8-sig").readlines()
    data_plus_plus1= open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    higest= len(data_plus_plus1)-1

    all_foter_homepage= ''
    for data_plus_plu in data_plus_plus:
        state= data_plus_plu.strip()
        short_url= short_code_state(state).lower()
        replaced_data= home_page_template.replace('aloomaidstate', state).replace('aloomaidstaturl', f'{'-'.join(rootpath.rsplit('/', 1))}{short_url}/')
        all_foter_homepage += replaced_data

    selected_row=[]
    id1=0
    all_foter_homepage1= ''
    for data_plus_plu1 in range(higest):
        while True:
            picker= random.randint(0,higest)
            if picker in selected_row:
                pass
            else:
                break
    
        
        selected_row.append(picker)
        split_city= data_plus_plus1[picker].replace('\n', '').split(',')

 
        city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_p= split_city[3].title().replace('ï»¿', '').replace('"', '')
        population= int(split_city[8])
        if population < int(population_limit):
            continue

        
        short_url= short_code_state(state_p).lower()
        replaced_data1= home_page_template.replace('aloomaidstaturl', f'{'-'.join(rootpath.rsplit('/', 1))}{link_city}-{short_url}/').replace('aloomaidstate', city_p)
        all_foter_homepage1 += replaced_data1
        if data_plus_plu1==50:
            break
        id1+=1
        if id1==50:
            break
    final_fotter= template_data_2.replace('aloomaidallfotter', all_foter_homepage).replace('aloomaidallfottecity', all_foter_homepage1)
    return final_fotter


def read_root_file(file_name):
    save_file= file_name.replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
    save_file= str(save_file.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
    fp = open(f'static/aloomaspecial/records/{save_file}.txt', "r", encoding="utf-8-sig").read()
    return fp

def state_url_data(state_rep, state_abbr_short, radioselect, population_limit, Pages_created_options, Checkboxselected, rootpath):
    def random_p(hrml_crens_one, picker_rand, col_nini):
        data= hrml_crens_one[picker_rand].replace('\n', '')
        if '$$' in data:
            return hrml_crens_one[picker_rand].replace('\n', '').split('$$')[col_nini].replace('ï»¿', '')
            
        else:
            return hrml_crens_one[picker_rand].replace('\n', '').split(',')[col_nini].replace('ï»¿', '')
    
    def all_state_url(state_rep, Checkboxselected):
        v= ''
        city_data= ''
        adeola=0
        selected_row=[]
        id1=0
        hrml_crens_one = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
       
        for city in hrml_crens_one:
            if not city.strip():
                continue
            
            split_city= city.replace('\n', '').split(',')
            city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
            sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_p= split_city[3].title().replace('ï»¿', '').replace('"', '')
            population= int(split_city[8])
            state_repl= split_city[3].title().replace('ï»¿', '').replace('"', '')
            if population < int(population_limit):
                continue

            if 'All Pages' == Pages_created_options:
                pass
            elif 'Selected State Pages' == Pages_created_options:
                if state_repl in Checkboxselected:
                    pass
                else:
                    continue
            elif 'Excluded State Pages' == Pages_created_options:
                if state_repl in Checkboxselected:
                    continue
                else:
                    pass
            
            if state_rep.lower() == state_p.lower() or state_rep.lower()[:5] == state_p.lower():
                
                v+= home_page_template.replace('aloomaidstaturl', f'{'-'.join(rootpath.rsplit('/', 1))}{link_city}-{state_abbr_short.lower()}/').replace('aloomaidstate', city_p)
                adeola += 1
                if adeola< 10:
                    while True:
                        picker_rand= random.randint(0,len(hrml_crens_one)-1)
                        if picker_rand in selected_row:
                            pass
                        else:
                            break
                    selected_row.append(picker_rand)
                    city_data+= f'{random_p(hrml_crens_one, picker_rand, 0)}, '
            
                id1+=1
                if id1==30:
                    break
                

        return v, city_data
    

    def all_county_url(state_rep):
        v= ''
        county_data= ''
        adeola=0
        selected_row=[]
        id1=0
        hrml_crens_one = open("static/aloomaspecial/content/county.txt", "r", encoding="windows-1254").readlines()
        for county in hrml_crens_one:
            if not county.strip():
                continue
            split_county= county.replace('\n', '').split('$$')
            county_p= split_county[0].replace('ï»¿', '').title()
            sub_county= county_p.replace(' ', '-').replace(',', '').replace('.', '').lower()
            sub_county= str(sub_county.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_p= split_county[1].replace('ï»¿', '')

            
            if state_rep.lower() == state_p.lower() or state_rep.lower()[:5] == state_p.lower():
                v+= home_page_template.replace('aloomaidstaturl', f'{'-'.join(rootpath.rsplit('/', 1))}{sub_county}-{state_abbr_short.lower()}/').replace('aloomaidstate', county_p)
                adeola += 1
                if adeola< 10:
                    while True:
                        picker_rand= random.randint(0,len(hrml_crens_one)-1)
                        if picker_rand in selected_row:
                            pass
                        else:
                            break
                    selected_row.append(picker_rand)
                    county_data+= f'{random_p(hrml_crens_one, picker_rand, 0)}, '

                id1+=1
                if id1==30:
                    break
        return v, county_data
    
    all_table_data1, rand_city= all_state_url(state_rep, Checkboxselected)
    if 'Yes'== radioselect:
        all_table_data2, rand_county= all_county_url(state_rep)
    else:
        all_table_data2= ''
        rand_county= ''

    return all_table_data1, rand_city, all_table_data2, rand_county

def random_state_webpage(confirm_state_pages):
    return open(confirm_state_pages, "r", encoding="utf-8-sig").read()

def city_url_data(data_usage, data_usage1, state_abbr_short, population_limit, Pages_created_options, Checkboxselected, rootpath):
    iframe= data_usage1.replace('"<iframe', '<iframe').replace('</iframe>"', '</iframe>')
    state_abbr_short= state_abbr_short.lower()
    split_usage= data_usage.replace('\n', '').replace('ï»¿', '').split('$$')
    county_web_contents= split_usage[1]
    all_table_data=''
    id=0
    hrml_crens_one = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    higest= len(hrml_crens_one)-1
       
    selected_row=[]
    for data_plus_plu1 in range(higest):
        while True:
            picker= random.randint(0,higest)
            if picker in selected_row:
                pass
            else:
                break
        selected_row.append(picker)
        split_city= hrml_crens_one[picker].replace('\n', '').split(',')

        city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_repl= split_city[3].title().replace('ï»¿', '').replace('"', '')
        population= int(split_city[8])
        state_abbr_sho = split_city[2].replace('ï»¿', '')

        if state_abbr_sho.lower() == state_abbr_short:
            pass
        else:
            continue

        if population < int(population_limit):
            continue

        if 'All Pages' == Pages_created_options:
            pass
        elif 'Selected State Pages' == Pages_created_options:
            if state_repl in Checkboxselected:
                pass
            else:
                continue
        elif 'Excluded State Pages' == Pages_created_options:
            if state_repl in Checkboxselected:
                continue
            else:
                pass

        all_table_data += home_page_template.replace('aloomaidstaturl', f'{'-'.join(rootpath.rsplit('/', 1))}{link_city}-{state_abbr_short.lower()}/').replace('aloomaidstate', city_p)
        id+=1
        if id==50:
            break


    return county_web_contents, all_table_data, iframe

def clean_text(cntents):
    soup = BeautifulSoup(cntents, 'html.parser')
    clean_text = soup.get_text()
    return clean_text

def county_url_data(data_usage, state_short_code_county, rootpath):
    state_short_code_county= state_short_code_county.lower()
    split_usage= data_usage.replace('\n', '').replace('ï»¿', '').split('$$')
    county_web_contents= split_usage[1]
    county_zip_code_all= split_usage[2]
    all_table_data=''
    id1=0
    all_data= county_zip_code_all.split('</tr><tr>')
    for all_dat in all_data:
        if not all_dat.strip():
            continue
        
        county_name= all_dat.split('</a></td>')[0]
        county_name= clean_text(county_name)
        sub_ciy= county_name.replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        zip= all_dat.split('</a></td>')[1]
        zip= clean_text(zip)
        all_table_data+= home_page_template1.replace('aloomaidcityname', county_name).replace('aloomaidzipcode', zip).replace('aloomaidcityurl', f'{'-'.join(rootpath.rsplit('/', 1))}{sub_ciy}-{state_short_code_county.lower()}/')
        id1+=1
        if id1==50:
            break
    return county_web_contents, all_table_data

def random_city_webpage(confirm_city_pages):
    return open(confirm_city_pages, "r", encoding="utf-8-sig").read()

def random_county_webpage(confirm_county_pages):
    return open(confirm_county_pages, "r", encoding="utf-8-sig").read()

def create_sitemape_page(sitemaps, rootpath):
    try:
        parent_dir5 = f"sitemap.xml"
        f = open(parent_dir5, "a", encoding='utf-8-sig', errors='replace')
        for site in sitemaps:
            f.write(site + '\n')
        f.close()
    except:
        pass
    
def create_home_page_url(confirm_home_pages, domain_site_name, rootpath, phone_number, Long_formurl, shortformurl, site_name, randomize_image, all_refomated_body):
    
    template_data_3 = open("static/aloomaspecial/metatitledescription.txt", "r", encoding="utf-8-sig").read()
    metatitle_homepage= read_root_file('Home Page Meta title')
    metadescription_homepage= read_root_file('Home Page Meta Description')
    complate_header= template_data_3.replace('aloomaidtitle', metatitle_homepage).replace('aloomaiddescription', metadescription_homepage).replace('aloomaiddomainname', f'https://{domain_site_name}/').replace('aloomaidsitename', site_name)
    full_home_page_contents= read_root_file('Home Page Contents').replace('#State', f'USA')
    replaced_entities= processing_handler.replace('#State', f'USA').replace('aloomaphonenumberid', phone_number).replace('aloomalongformid', Long_formurl).replace('aloomashortformid', shortformurl).replace('aloomasitenameid', domain_site_name).replace('aloomalistofimagesid', f'{randomize_image}').replace('aloomaspintaxcontentsid', full_home_page_contents) + all_refomated_body
    home_page= random_homepage_webpage(confirm_home_pages).replace('<title></title>', complate_header).replace('<meta content="" name="keywords">', '').replace('<meta content="" name="description">', '').replace('aloomaiddomainname', f'https://{domain_site_name}/').replace('</head>', '<link rel="stylesheet" href="static/aloomaspecial/alooma.css"><link rel="stylesheet" href="static/aloomaspecial/alooma2.css"></head>').replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l').replace('#State', f'USA').replace('aloomaidbody', replaced_entities)
    fp = open(f'index.html', "w", encoding='utf-8-sig')
    fp.writelines(home_page)
    fp.close()

    return f'<url><loc>https://{domain_site_name}/</loc></url>'

def create_state_url(state_name, confirm_state_pages, domain_site_name, state_abbr_short, all_table_dat1, all_table_dat2, rand_cty, rand_cunty, rootpath, phone_number, Long_formurl, shortformurl, site_name, randomize_image):
    state_abbr_short= state_abbr_short.lower()
    try:
        os.makedirs(f'{rootpath.replace('/', '')}-{state_abbr_short}') 
    except:
        pass
    state_name= state_name.replace("'", '')
    
    if all_table_dat2=='':
        state_page= random_state_webpage(confirm_state_pages).replace('<meta content="" name="keywords">', '').replace('<meta content="" name="description">', '').replace('aloomaiddomainname', f'https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{state_abbr_short}/').replace(county_remove, '').replace('aloomaidstatecity', all_table_dat1).replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l').replace('#State', f'{state_name}, {state_abbr_short.upper()}').replace('[listcountycity]', f'{rand_cty}, {rand_cunty}').replace('aloomaiddomainname', f'https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{state_abbr_short}/')
    else:
        state_page= random_state_webpage(confirm_state_pages).replace('<meta content="" name="keywords">', '').replace('<meta content="" name="description">', '').replace('aloomaiddomainname', f'https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{state_abbr_short}/').replace('aloomaidstatecounty', all_table_dat2).replace('aloomaidstatecity', all_table_dat1).replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l').replace('#State', f'{state_name}, {state_abbr_short.upper()}').replace('[listcountycity]', f'{rand_cty}, {rand_cunty}').replace('aloomaiddomainname', f'https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{state_abbr_short}/')
    
    fp = open(f'{rootpath.replace('/', '')}-{state_abbr_short}/index.html', "w", encoding='utf-8-sig')
    fp.writelines(state_page)
    fp.close()
    

    return state_name, f'<url><loc>https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{state_abbr_short}/</loc></url>'


def create_city_page_url(state_name, url_state_structure, state_abbr_short, city_name, url_city_structure, confirm_city_pages, domain_site_name, county_web_contents1, all_table_data1, iframe, zip, rootpath, phone_number, Long_formurl, shortformurl, site_name, randomize_image):
    state_abbr_short= state_abbr_short.lower()
    try:
        os.makedirs(f'{rootpath.replace('/', '')}-{url_city_structure}-{state_abbr_short}') 
    except:
        pass
    city_name= city_name.replace("'", '')
    metatitle_citypage= read_root_file('City Page Meta Title').split('@@@')
    picker_metatitle_citypage= random.randint(0, len(metatitle_citypage)-1)
    metatitle_citypage= metatitle_citypage[picker_metatitle_citypage]

    metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(metadescription_citypage)-1)
    metadescription_citypage= metadescription_citypage[picker_metadescription_citypage]

    metatitle_citypage_one= read_root_file('City Page Meta Title')
    metadescription_citypage_one= read_root_file('City Page Meta Description')
    metatiledescription_data= metatileanddescripttion.replace('{{aloomaidtitle}}', metatitle_citypage_one).replace('{{aloomaiddescription}}', metadescription_citypage_one)

    full_city_page_contents= read_root_file('City Page Contents').replace('#State', f'{city_name}, {state_abbr_short.upper()}').replace('#City', f'{city_name}, {state_abbr_short.upper()}')
    replaced_entities= processing_handler.replace('#State', f'{city_name}, {state_abbr_short.upper()}').replace('#City', f'{city_name}, {state_abbr_short.upper()}').replace('aloomaphonenumberid', phone_number).replace('aloomalongformid', Long_formurl).replace('aloomashortformid', shortformurl).replace('aloomasitenameid', domain_site_name).replace('aloomalistofimagesid', f'{randomize_image}'.replace('static/', '../static/')).replace('aloomaspintaxcontentsid', full_city_page_contents)
    city_page= random_city_webpage(confirm_city_pages).split('@@@')
    picker_city_page= random.randint(0, len(city_page)-1)
    city_page= city_page[picker_city_page]

    city_page= city_page.replace('</head>', metatiledescription_data).replace('{{aloomaidtitle}}', metatitle_citypage).replace('{{aloomaiddescription}}', metadescription_citypage).replace('<meta content="" name="keywords">', '').replace('<meta content="" name="description">', '').replace('aloomaidcontentscity', county_web_contents1).replace('aloomaidcitycloseto', all_table_data1).replace('aloomaidzip', zip).replace('aloomaidembeddedmap', iframe).replace('#State', f'{city_name}, {state_abbr_short.upper()}').replace('"../static/', '"../static/').replace('aloomaiddomainname', f'https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{url_city_structure}-{state_abbr_short}/').replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l').replace('{{aloomaidbody}}', replaced_entities)
    fp = open(f'{rootpath.replace('/', '')}-{url_city_structure}-{state_abbr_short}/index.html', "w", encoding='utf-8-sig')
    fp.writelines(city_page)
    fp.close()
    
    return f'<url><loc>https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{url_city_structure}-{state_abbr_short}/</loc></url>'



def create_county_page_url(state_name, url_state_structure, state_abbr_short, county_name, url_county_structure, confirm_county_pages, domain_site_name, county_web_contents2, all_table_data2, rootpath, phone_number, Long_formurl, shortformurl, site_name, randomize_image):
    state_abbr_short= state_abbr_short.lower()
    try:
        os.makedirs(f'{rootpath.replace('/', '')}-{url_county_structure}-{state_abbr_short}') 
    except:
        pass
    county_name= county_name.replace("'", '')

    metatitle_countypage= read_root_file('County Page Meta Title').split('@@@')
    picker_metatitle_countypage= random.randint(0, len(metatitle_countypage)-1)
    metatitle_countypage= metatitle_countypage[picker_metatitle_countypage]

    metadescription_countypage= read_root_file('County Page Meta Description').split('@@@')
    picker_metadescription_countypage= random.randint(0, len(metadescription_countypage)-1)
    metadescription_countypage= metadescription_countypage[picker_metadescription_countypage]

    metatitle_countypage_one= read_root_file('County Page Meta Title')
    metadescription_countypage_one= read_root_file('County Page Meta Description')
    metatiledescription_data= metatileanddescripttion.replace('{{aloomaidtitle}}', metatitle_countypage_one).replace('{{aloomaiddescription}}', metadescription_countypage_one)

    county_page= random_county_webpage(confirm_county_pages).split('@@@')
    picker_county_page= random.randint(0, len(county_page)-1)
    county_page= county_page[picker_county_page]

    full_county_page_contents= read_root_file('City Page Contents').replace('#State',  f'{county_name}, {state_abbr_short.upper()}').replace('#County', f'{county_name}, {state_abbr_short.upper()}').replace('#City', f'{county_name}, {state_abbr_short.upper()}')
    replaced_entities= processing_handler.replace('#State',  f'{county_name}, {state_abbr_short.upper()}').replace('#County', f'{county_name}, {state_abbr_short.upper()}').replace('#City', f'{county_name}, {state_abbr_short.upper()}').replace('aloomaphonenumberid', phone_number).replace('aloomalongformid', Long_formurl).replace('aloomashortformid', shortformurl).replace('aloomasitenameid', domain_site_name).replace('aloomalistofimagesid', f'{randomize_image}'.replace('static/', '../static/')).replace('aloomaspintaxcontentsid', full_county_page_contents)

    county_page= county_page.replace('</head>', metatiledescription_data).replace('{{aloomaidtitle}}', metatitle_countypage).replace('{{aloomaiddescription}}', metadescription_countypage).replace('<meta content="" name="keywords">', '').replace('<meta content="" name="description">', '').replace('aloomaidcountycontents', county_web_contents2).replace('aloomaidcountytable', all_table_data2).replace('#State',  f'{county_name}, {state_abbr_short.upper()}').replace('"../static/', '"../static/').replace('aloomaiddomainname', f'https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{url_county_structure}-{state_abbr_short}/').replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l').replace('{{aloomaidbody}}', replaced_entities)
    
    fp = open(f'{rootpath.replace('/', '')}-{url_county_structure}-{state_abbr_short}/index.html', "w", encoding='utf-8-sig')
    fp.writelines(county_page)
    fp.close()
    
    return f'<url><loc>https://{domain_site_name}{'-'.join(rootpath.rsplit('/', 1))}{url_county_structure}-{state_abbr_short}/</loc></url>'

def all_pages_protocol():
    domain_site_name= read_root_file('Domain Site')
    population_limit= read_root_file('Population limit')
    radioselect= read_root_file('Do you need County Page')
    site_root= read_root_file('Site Root')
    phone_number= read_root_file('Phone Number')
    Long_formurl= read_root_file('Long Form')
    shortformurl= read_root_file('Short Form')
    site_name= read_root_file('Site Name')
    randomize_image= read_root_file('Randomized image File root').split(',')

    c=0
    duplicate_state=[]
    sitemaps = []
    sitemaps.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    confirm_state_pages= f'allrequiredpages/state.html'
    confirm_city_pages= f'allrequiredpages/city.html'
    confirm_county_pages= f'allrequiredpages/county.html'
    confirm_home_pages= f'allrequiredpages/homepage.html'
    all_refomated_body=  home_page_footer(population_limit, site_root)

# -----------------------------------------------------------------------------------------------
    sitemaphomepageurl= create_home_page_url(confirm_home_pages, domain_site_name, site_root, phone_number, Long_formurl, shortformurl, site_name, randomize_image, all_refomated_body)
    sitemaps.append(sitemaphomepageurl)


# -----------------------------------------------------------------------------------------------
    naimah=0
    city_contents_data = open("static/aloomaspecial/content/content.csv", "r", encoding="utf-8-sig").readlines()
    city_embedded_data = open("static/aloomaspecial/content/mapembedded.txt", "r", encoding="utf-8-sig").readlines()
    search_categories = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        sub_ciy_repl= credential[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= credential[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_abbr_short = credential[2].replace('ï»¿', '')
        state_repl= credential[3].title().replace('ï»¿', '').replace('"', '')
        state= credential[3].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        population= int(credential[8])
        zip_codes= credential[15]
        if 'Puerto Rico'.replace(' ', '-').lower() == state:
            continue
        elif 'Virgin Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Washington, D.C.'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Pacific'.replace(' ', '-').lower() == state:
            continue
        elif 'American Samoa'.replace(' ', '-').lower() == state:
            continue
        elif 'Guam'.replace(' ', '-').lower() == state:
            continue
        elif 'Palau'.replace(' ', '-').lower() == state:
            continue
        elif 'Federated States of Micronesia'.replace(' ', '-').lower() == state:
            continue
        elif 'Northern Mariana Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Marshall Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Europe'.replace(' ', '-').lower() == state:
            continue
        else:
            pass
        
        if population < int(population_limit):
            continue
        
        if state_repl in duplicate_state:
            pass
        else:
            c +=1
            all_table_dat1, rand_cty, all_table_dat2, rand_cunty= state_url_data(state_repl, state_abbr_short, radioselect, population_limit, 'All Pages', [], site_root)
            check_state, sitemapstateurl= create_state_url(state_repl, confirm_state_pages, domain_site_name, state_abbr_short, all_table_dat1, all_table_dat2, rand_cty, rand_cunty, site_root, phone_number, Long_formurl, shortformurl, site_name, randomize_image)
            duplicate_state.append(check_state)
            sitemaps.append(sitemapstateurl)
 
        c +=1
        county_web_contents1, all_table_data1, iframe= city_url_data(city_contents_data[naimah], city_embedded_data[naimah], state_abbr_short, population_limit, 'All Pages', [], site_root)
        naimah+=1
        sitemapcityurl= create_city_page_url(state_repl, state, state_abbr_short, sub_ciy_repl, sub_ciy, confirm_city_pages, domain_site_name, county_web_contents1, all_table_data1, iframe, zip_codes, site_root, phone_number, Long_formurl, shortformurl, site_name, randomize_image)
        sitemaps.append(sitemapcityurl)
        
        
    
# -----------------------------------------------------------------------------------------------
    if 'Yes'== radioselect:
        nini=0
        county_embedded_data = open("static/aloomaspecial/content/content1.csv", "r", encoding="utf-8-sig").readlines()
        search_categories1 = open("static/aloomaspecial/content/county.txt", "r", encoding="utf-8").readlines()
        for credentials1 in search_categories1:
            if not credentials1.strip():
                continue
            
            credential1= credentials1.strip().split('$$')
            county_repl= credential1[0].title().replace('ï»¿', '').replace('"', '')
            county= credential1[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            county= str(county.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            
            state_repl= credential1[1].title().replace('ï»¿', '')
            state= credential1[1].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_short_code_county= short_code_state(state_repl)
            county_web_contents2, all_table_data2= county_url_data(county_embedded_data[nini], state_short_code_county, site_root)
            
            nini+=1
            c +=1
            sitemapcountyurl= create_county_page_url(state_repl, state, state_short_code_county, county_repl, county, confirm_county_pages, domain_site_name, county_web_contents2, all_table_data2, site_root, phone_number, Long_formurl, shortformurl, site_name, randomize_image)
            sitemaps.append(sitemapcountyurl)
            
    else:
        pass

    sitemaps.append('</urlset>')
    
#-------------------------------------------------------------------------------------------------
    create_sitemape_page(sitemaps, site_root)
    

all_pages_protocol()
