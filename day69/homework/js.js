//   2) დაწერე პროგრამა, რომელიც მომხმარებლისგან შეიტანს სტუდენტის მიღებულ ქულას (0-დან 100-მდე) და if-else პირობით
//     გამოიტანს შესაბამის ნიშანს შემდეგი წესით:

//     ქულა ნიშანი
//     90 – 100 A
//     80 – 89 B
//     70 – 79 C
//     60 – 69 D
//     0 – 59 F


let score = 100;

if (score >= 90 && score <= 100) {
    console.log("ნიშანი A")
} else if (score >= 80 && score <= 89) {
    console.log("ნიშანი B")
} else if (score >= 70 && score <= 79) {
    console.log("ნიშანი C")
} else if (score >= 60 && score <= 69) {
    console.log("ნიშანი D")
} else if (score >= 0 && score <= 59) {
    console.cog("ნიშანი F")
} else {
    console.log("ქულა არასწორია")
}


//  3) მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში.
//     თუ ტემპერატურა 0-ზე ნაკლებია → დაპრინტეთ “Cold ❄️”,
//     თუ 0–30 შორისაა → დაპრინტეთ “Normal 🌤️”,
//     თუ 30-ზე მეტია → დაპრინტეთ “Hot ☀️”.


let temp = 100

if (temp <= 0) {
    console.log("Cold ❄️");
} else if (temp >= 30) {
    console.log("Normal 🌤️")
} else {
    console.log("Hot ☀️");
}



// 4) მოცემულია ცვლადი:

//     let isLoggedIn = true;

//     მხოლოდ Ternary ოპერატორის გამოყენებით შეამოწმეთ isLoggedIn ცვლადის მნიშვნელობა. თუ ის true-ს უდრის, console-ში
//     გამოიტანეთ ტექსტი "Welcome Back!", ხოლო თუ false-ია — "Please Log In".


let isLoggedIn = true;

isLoggedIn ? "Welcome Back!" : "Please Log In"

console.log(isLoggedIn)



//  5) შემქენით ცვლადი year სადაც შეიყვანთ რაღაც წელიწადს. შეამოწმე ეს წელი ნაკიანი წელია თუ არა.



 


