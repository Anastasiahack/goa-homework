// 2) კომენტარების სახით ახსენით თუ რა არის scope ბი, რაში გვადგება, და მოიყვანეთ ერთი ცხოვრებისეული მაგალითი

// scope არის ადგილი სადაც შესაძლებელია გამოვიყენოთ ცვლადები და დავაბრუნოთ მნიშვნელობა ,
// scope - ის ბლოკის არეალის განსახღვრისას ცნობილია რომელ  ბლოკში ხდება ცვლადის declaration და initialization,Asigment ,
// ბლოკი არის კოდის ნაწილი რომელიც იწერება curlu braces { } - ფიგურულ ფრჩხილებში 



// 3) ახსენით scopeბის ორი ტიპი კომენტარების სახით, მათი დანიშნულება და თითო მაგალითი რეალური ცხოვრებიდან

// scope - ბს აქვს ორი ძირითადი ტიპი Block scope end Global scope :

// Global scope როდესაც ცვლადი არის გობალურად ხელმისაწვდომი და არ შედის უშვალოდ ბლოკის არეალში ,
// Block scope როდესაც ცვლადი  უშვალოდ ბლოკის არეალში არის ხელმისაწვდომი 

// მაგალითი :
// მაგალითად როდესაც სამყაროს რაღაც ნაწილს ხედავ 1-დან 4-განზომილების ჩათვლით ეს არის Block scope რადგან ამ ქვედა განზომილებებში 
// არ არის შესაძლებელი სამყაროს გარკვეული მთლიანი ნაწილის აღქმა ყველა განზომილებაში სხვადასხვა ნაირად ხდება სივრცის აღქმა რაც გავს 
// Block scope -ს რადგან ცვლადები რომლებიც ბლოკში არიან მოქცეულნნი სწორედ ამ განზომილებებს გავნან სივრცის არეალის თვალსაზრისით ხოლო
// Global scope - ის მაგალიტ იქნება მეხუთე განზომილებიდან დაწყებული უსასრულოდ რადგან მეხუტე განზომილება არის დუალური და მისი ყოველ მხრივ 
// აღქმა ხდება შესაძლებებლი როგორც Global scope - ის ცვლადი რომელიც მთლიან პროგრამაშია ხელმისაწვდომი 


// 4) გააკეთეთ 2-2 პრაქტიკული მაგალითი Block და Global scope ბზე

// Bllock scope

function Obtainingdriverslicensecategory(carCategory, age) {

    if (carCategory === "E") {
        const minAge = 21;
        if (age >= minAge) {
            console.log("თქვენ აიღეთ " + carCategory + " კატეგორიის მართვის მოწმობა");
        } else {
            console.log(carCategory + " კატეგორიისთვის მინიმუმ " + minAge + " წლის უნდა იყოთ");
        }
    } else if (carCategory === "B") {
        const minAge = 17;
        if (age >= minAge) {
            console.log("თქვენ აიღეთ " + carCategory + " კატეგორიის მართვის მოწმობა");
        } else {
            console.log(carCategory + " კატეგორიისთვის მინიმუმ " + minAge + " წლის უნდა იყოთ");
        }
    } else if (carCategory === "C") {
        const minAge = 18;
        if (age >= minAge) {
            console.log("თქვენ აიღეთ " + carCategory + " კატეგორიის მართვის მოწმობა");
        } else {
            console.log(carCategory + " კატეგორიისთვის მინიმუმ " + minAge + " წლის უნდა იყოთ");
        }
    } else if (carCategory === "D") {
        const minAge = 21;
        if (age >= minAge) {
            console.log("თქვენ აიღეთ " + carCategory + " კატეგორიის მართვის მოწმობა");
        } else {
            console.log(carCategory + " კატეგორიისთვის მინიმუმ " + minAge + " წლის უნდა იყოთ");
        }
    } else if (carCategory === "E") {
        const minAge = 21;
        if (age >= minAge) {
            console.log("თქვენ აიღეთ " + carCategory + " კატეგორიის მართვის მოწმობა");
        } else {
            console.log(carCategory + " კატეგორიისთვის მინიმუმ " + minAge + " წლის უნდა იყოთ");
        }
    } else {
        console.log(carCategory + " ასეთი კატეგორია არ არსებობს");
    }
}

Obtainingdriverslicensecategory("E", 21);


// Global scope




const UserGe='Ka'

function geoMessage(){
    if (UserGe === 'Ka'){
        console.log('geo ka')
    }
}

geoMessage()

