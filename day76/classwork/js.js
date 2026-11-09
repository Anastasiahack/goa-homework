// 1) შექმენი Array სახელად cars, რომელშიც შეინახავ 5 სხვადასხვა მანქანის ბრენდს.:
//   1. გამოიტანე კონსოლში პირველი ელემენტი.
//   2. გამოიტანე კონსოლში მესამე ელემენტი.
//   3. გამოიტანე კონსოლში ბოლო ელემენტი.
//   4. სცადე ისეთი ინდექსის გამოძახება, რომელიც Array-ში არ არსებობს. რას გამოიტანს JavaScript?
//   5. შექმენი String სახელად word და შეინახე მასში სიტყვა "JavaScript".
// გამოიტანე კონსოლში მეოთხე ინდექსზე მდგომი სიმბოლო.


let cars=["mersedes", "beenve",  "porhe", "EVO", "jeep"]

console.log(cars[0])

console.log(cars[2])

console.log(cars[4])

console.log(cars[777])

const word="JavaScript"

console.log(word[4])





// 2) შექმენი შემდეგი Array:
// const fruits = ["Apple", "Banana", "Orange", "Kiwi", "Mango"];


// შეასრულე შემდეგი მოქმედებები:
// 1. შეცვალე პირველი ელემენტი "Peach"-ით.
// 2. შეცვალე მესამე ელემენტი "Watermelon"-ით.
// 3. შეცვალე ბოლო ელემენტი "Cherry"-ით.
// 4. გამოიტანე მთლიანი Array კონსოლში.
// 5. გამოიტანე მხოლოდ მეორე ელემენტი.



const fruits = ["Apple", "Banana", "Orange", "Kiwi", "Mango"];


fruits[0]="Peach"
fruits[2]="Watermelon"
fruits[4]="Cherry"

console.log(fruits)

console.log(fruits[1])





// 3) შექმენი ორი Array:
// let students = ["Giorgi", "Nika", "Ana"];

// const teachers = ["David", "Maria", "John"];


// შეასრულე შემდეგი მოქმედებები:
// 1. students Array-ში შეცვალე პირველი ელემენტი "Luka"-ით.
// 2. მთლიანად გადაწერე students Array ახალი მნიშვნელობებით.
// 3. teachers Array-ში შეცვალე მეორე ელემენტი "George"-ით.

let student = ["Giorgi", "Nika", "Ana"];

const teachers = ["David", "Maria", "John"];


console.log(student["Luka"])

student=["Kungfu","panda","shifu"]

teachers[1]="George"

console.log(student)



console.log(teachers)






