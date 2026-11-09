// 2) შექმენი Array სახელად movies, რომელშიც შეინახავ 6 საყვარელი ფილმის სახელს.

// შეასრულე შემდეგი მოქმედებები:
// 1. გამოიტანე პირველი და ბოლო ფილმის სახელი.
// 2. გამოიტანე Array-ის მესამე ელემენტი.
// 3. შეცვალე მეორე ფილმი სხვა ფილმით.
// 4. შეცვალე მეხუთე ფილმი სხვა ფილმით.
// 5. გამოიტანე მთლიანი Array.
// 6. გამოიტანე Array-ის ელემენტების რაოდენობა .length-ის გამოყენებით.

// მთვრალი ოსტატი, Dark Matter, Kung Fu Panda, Alionedi, Matrix,  Ip Man (2008), 
//   Ip Man 3 (2015) , 

let movies=["Dark Matter", "The 36th Chamber of Shaolin(1978)", " Kung Fu Panda",  
    "Matrix",  "Ip Man (2008)", "Ip Man 2 (2010)"]

console.log(movies[0], movies[5])

console.log(movies[2])

movies[1]=" Ip Man 4: The Finale (2019)"

movies[4]="Drunk master"

console.log(movies.length)

console.log(movies)




// 3) შექმენი Array სახელად shoppingList, რომელშიც შეინახავ 5 პროდუქტს.

// let shoppingList = ["Milk", "Bread", "Eggs", "Cheese", "Juice"];


// შეასრულე შემდეგი მოქმედებები:
// 1. დაამატე ორი ახალი პროდუქტი .push() მეთოდით.
// 2. წაშალე ბოლო პროდუქტი .pop() მეთოდით.
// 3. შეცვალე პირველი პროდუქტი "Chocolate"-ით.
// 4. გამოიტანე Array კონსოლში.
// 5. გამოიტანე პროდუქტების საბოლოო რაოდენობა.


let shoppingList = ["Milk", "Bread", "Eggs", "Cheese", "Juice"];

shoppingList.push("Avocado","Strawberry")

shoppingList.pop("Strawberry")

shoppingList[0]="Chocolate"

console.log(shoppingList)

console.log(shoppingList.length)





// 4) შექმენი Array სახელად myData, რომელშიც შეინახავ მინიმუმ 6 ელემენტს.

// Array-ში აუცილებლად უნდა იყოს:
// - String
// - Number
// - Boolean
// შეასრულე შემდეგი მოქმედებები:
// 1. გამოიტანე პირველი ელემენტი.
// 2. გამოიტანე მეოთხე ელემენტი.
// 3. შეცვალე რომელიმე String სხვა String-ით.
// 4. შეცვალე რომელიმე Number სხვა Number-ით.
// 5. დაამატე ახალი Boolean მნიშვნელობა .push()-ის გამოყენებით.
// 6. წაშალე ბოლო ელემენტი .pop()-ის გამოყენებით.
// 7. გამოიტანე საბოლოო Array და მისი სიგრძე.


let myData = ["JavaScript", 0, true, "Python", 100, false];

console.log(myData[0]);

console.log(myData[3]);

myData[0] = "HTML";

myData[1] = 50;

myData.push(true);

myData.pop();

console.log(myData);

console.log(myData.length);



// 5) მოცემულია:
// let cars = ["BMW", "Mercedes", "Audi"];

// const fruits = ["Apple", "Banana", "Orange"];


// შეასრულე შემდეგი მოქმედებები:
// 1. cars Array-ში შეცვალე პირველი ელემენტი "Toyota"-თი.
// 2. მთლიანად გადაწერე cars ახალი Array-ით.
// 3. fruits Array-ში შეცვალე მეორე ელემენტი "Kiwi"-თი.
// 4. დაამატე fruits Array-ში "Mango" .push() მეთოდით.
// 5. წაშალე fruits Array-ის ბოლო ელემენტი .pop() მეთოდით.
// 6. სცადე fruits მთლიანად გადაწერო ახალი Array-ით.

let cars = ["BMW", "Mercedes", "Audi"];

const fruits = ["Apple", "Banana", "Orange"];

let niucars=[...cars]

cars[0]="Toyota"

fruits[1]="Kiwi"

console.log(fruits.push("Mango"))

console.log(niucars)

console.log(fruits.pop())

let niufruits=[...fruits]




// 6) რა განსხვავებაა let-ით და const-ით შექმნილ Array-ებს შორის?

// რომ let-ით შექმნილ ცვლადს შეგიძლია ახალი Array მიანიჭო, ხოლო const-ით შექმნილს — არა.
// მაგრამ ორივე შემთხვევაში შესაძლებელია Array-ის ელემენტების შეცვლა, დამატება და წაშლა.