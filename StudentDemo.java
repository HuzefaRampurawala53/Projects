import java.util.Scanner;

// Class definition
class Student {
    // Attributes (data members)
    String name;
    int rollNumber;
    float marks;

    // Method to input student details
    void inputDetails(Scanner sc) {  // pass Scanner from main, so it won't be closed early
        System.out.print("Enter name: ");
        name = sc.nextLine();

        System.out.print("Enter roll number: ");
        rollNumber = sc.nextInt();

        System.out.print("Enter marks: ");
        marks = sc.nextFloat();
        sc.nextLine();  // consume leftover newline
    }

    // Method to display student details
    void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Marks: " + marks);
        System.out.println();
    }
}

// Main class
public class StudentDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Creating two Student objects
        Student student1 = new Student();
        Student student2 = new Student();

        // Taking input for both students
        System.out.println("Enter details for Student 1:");
        student1.inputDetails(sc);

        System.out.println("\nEnter details for Student 2:");
        student2.inputDetails(sc);

        // Displaying details of both students
        System.out.println("\nStudent Details:");
        student1.displayDetails();
        student2.displayDetails();

        sc.close();
    }
}
