task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ")
message1 = 'that requires immediate attention today!'
message2 = "Consider completing it when you have free time"


match priority:
    
    case 'high':
        if time_bound in ('yes'):
            print(f"Reminder: '{task}' is a high priority task that {message1}")
        elif time_bound in ('no'):
            print(f"Note: '{task}' is a low priority task. {message2}.")

    case 'medium':
        if time_bound in ('yes'):
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        elif time_bound in ('no'):
            print(f"Note: '{task}' is a low priority task. {message2}.")

    case 'low':
        if time_bound in ('yes'):
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        elif time_bound in ('no'):
            print(f"Note: '{task}' is a low priority task. {message2}.")