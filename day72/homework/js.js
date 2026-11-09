// 2) ახსსენით დღეს ნასწავლი ფუნქციის ტიპები კომენტარების სახით:

// helper functions-არის დამხმარე ფუნქცია მთავარუ დუდუ ფუნქციისთვის ანუ helper functions-ით შესაძლებელია ერთ ფუნქციაში
//  მეოტე ფუნქციის გამოძახება და ტერმინალში შედეგის გამოტანა 

// arrow functions-არის ფუნქციის წერის შემოკლებული მეთოდი რომლის გამოყენებისას შეგვიძლია საერთოდ ერთ ხაზში დავწეროთ ფუნქცია რეთურნის გარეშედაც შესაძკებეკუა წერა თუ მხოლოდ ერთი 
// მოქმედება არის შესასრულებელი functuin-ისგან განსხვავებით ბევრად მოკლედ არის შესაძლებეელი ფუნქციის შექმნა მაგრამ ჩეულებრივ
// functuin-ისგან განსხვავებით arrow functions-ზე არ მოქმედებს Hoistimgi და ამოაგფრბს შეცდომას (ReferenceError ან TypeError)


// 3) ახსენით თუ რა არის return keyword და რაში გამოიყენება:
// return არის საკვანძო სიტყვა (Keyword) პროგრამირებაში (მათ შორის JavaScript-სა და Python-ში), რომელიც 
// გამოიყენება ფუნქციიდან შედეგის გამოსატანად /დასაბრუნებლად.
// ფუნქციაში retur-ის შემდეგ აღარაფერი იწერება რადგან retur-ის დაწერის შემდგომ ფუნქცია დამთავრებულია  


// 4) შექმენით 4 ფუნქცია, add, subtract, division და multiplication function keyword გამოყენებით და გადაეცით 2-2 პარამეტრი ყველა 
// ფუნქციას, თქვენი დავალებაა რომ გამოიყენოთ return keyword, გადაეცით ამ ფუნქციებს რიცხვები და გამოიტანეთ თითოეული ფუნქციის შედეგი

function add(a, b) {
  return a + b;
}


function subtract(a, b) {
  return a - b;
}


function division(a, b) {
  return a / b;
}


function multiplication(a, b) {
  return a * b;
}

console.log(add(10, 5));
console.log(subtract(10, 5));
console.log(division(10, 5));
console.log(multiplication(10, 5));



// 5) შექმენი მთავარი ფუნქცია, რომელიც მიიღებს მოსწავლის ქულას.

// გამოიყენე ორი helper function:

// 1. პირველი ფუნქცია შეამოწმებს, არის თუ არა ქულა 50-ზე მეტი.
// 2. მეორე ფუნქცია დააბრუნებს შესაბამის შეფასებას:
// 90 ან მეტი → "A"
// 70–89 → "B"
// 50–69 → "C"
// 50-ზე ნაკლები → "F"

// მთავარმა ფუნქციამ ეს helper functions უნდა გამოიყენოს და საბოლოოდ შეფასება დააბრუნოს.

// მაგალითად, 85 ქულაზე პასუხი უნდა იყოს "B".

function isPassing(score) {
  return score >= 50;
}


function getGrade(score) {
  if (score >= 90) {
    return "A";
  } else if (score >= 70) {
    return "B";
  } else if (score >= 50) {
    return "C";
  } else {
    return "F";
  }
}


function evaluateStudent(score) {

  const passed = isPassing(score);

  if (!passed) {

    return "F (ჩაიჭრა)";
  }


  return getGrade(score);
}

// ტესტირება:
console.log(evaluateStudent(85)); // დაიბეჭდება: B
console.log(evaluateStudent(95)); // დაიბეჭდება: A
console.log(evaluateStudent(40)); // დაიბეჭდება: F (ჩაიჭრა)
console.log(evaluateStudent(60)); // დაიბეჭდება: C



// 6) შექმენი ორი function expression:

// პირველი ფუნქცია მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს.
// მეორე ფუნქცია მიიღებს ერთ რიცხვს და შეამოწმებს, არის თუ არა ის ლუწი.

// შემდეგ შექმენი მთავარი ფუნქცია, რომელიც გამოიყენებს ორივე ფუნქციას.

// მაგალითად, თუ მთავარ ფუნქციას გადასცემ 5-სა და 7-ს, უნდა მიიღო:

// 12 — კენტია.

const totalNum = function (a, b) {
  return a + b;
};

const Evenorodd = function (num) {
  if (num % 2 == 0) {
    return "ლუწია";
  } else {
    return "კენტია";
  }
};

function main(a, b) {
  let total = totalNum(a, b);
  return total + " — " + Evenorodd(total);
}

console.log(main(5, 7));



// 7) შექმენი arrow function, რომელიც მიიღებს რიცხვს და დააბრუნებს:

// თუ რიცხვი დადებითია - "Positive"
// თუ უარყოფითია - "Negative"
// თუ 0-ია - "Zero"

// მაგალითად:

// checkNumber(5) - "Positive"
// checkNumber(-3) - "Negative"
// checkNumber(0) - "Zero"


// 8) შექმენი concise body arrow function, რომელიც მიიღებს რიცხვს და დააბრუნებს მის სამმაგ მნიშვნელობას.

// მაგალითად:

// triple(2) → 6
// triple(5) → 15
// triple(10) → 30

// პირობა: გამოიყენე concise body — {} და return არ გამოიყენო.