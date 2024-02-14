class Person {  // Parent class
    constructor(inName, inAge,) {
        // Properties
        this.name = inName;
        this.age = inAge;
    }

    sing = () => console.log("lalalalala");
}

class Employee extends Person {  // Child class extends the parent class (inherits from)
    constructor(name, age, position, department, salary) {
        // this.name = name;  // Could do it here... but...
        // this.age = age;
        super(name, age);  // Have the parent class initialize these, instead.

        this.position = position;
        this.department = department;
        this.salary = salary;
    }
}

const david = new Employee("David", 27, "CFO", "Finance", 100);
console.log("DAVID:", david);
david.sing();

class One { }
let oneFirst = new One();
console.log(oneFirst);

class Two extends One { }
let twoFirst = new Two();
console.log(twoFirst);

class Three extends Two {
    constructor() {
        super();
    }
}
let threeFirst = new Three();
console.log(threeFirst);

class Four extends Three { }
let fourFirst = new Four();
console.log(fourFirst);
