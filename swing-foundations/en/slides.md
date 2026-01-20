---
title: "Java Swing: Foundations of the UI and the Event Dispatch Thread"
theme: default
---

# Java Swing: Foundations of the UI and the Event Dispatch Thread
*Intermediate Java developers*

---

# Learning Objectives
- Master the Event-Driven Programming paradigm
- Understand the Event Dispatch Thread (EDT) lifecycle
- Apply the Golden Rule: All Swing operations on the EDT
- Recognize anti-patterns and implement best practices
- Build robust Swing applications using the Robust Skeleton pattern

<!--
These are the core competencies students will gain. Emphasize that EDT mastery is foundational for all Swing development.
-->

---

# The Event-Driven Paradigm
- Shift from procedural (sequential) to event-driven programming
- GUI apps wait in an infinite loop for OS-level events
- User actions (clicks, keystrokes) generate events
- The application responds by executing event handlers
- No predefined execution order - the user drives the flow

<!--
This is a fundamental mindset shift. Traditional console apps follow a linear script. GUI apps are reactive - they wait for user input and respond accordingly.
-->

---

# What is the Event Dispatch Thread?
- The EDT is Swing's single UI thread
- Handles ALL UI operations: creation, modification, rendering
- Processes events from the event queue (mouse, keyboard, repaint)
- Runs an infinite event loop until the application exits
- NOT the Main Thread - must be explicitly invoked

<!--
Key concept: Swing is single-threaded by design. The EDT is the heart of Swing - understanding it is non-negotiable.
-->

---
layout: center
---

# EDT Flow Diagram

![EDT Flow Diagram](/images/01-edt-flow-diagram.jpg)

- Event Queue receives OS events
- EDT pulls events and dispatches to listeners
- Components repaint and update state
- Cycle repeats indefinitely

<!--
Walk through the diagram step-by-step. Point out the queue, the dispatch loop, and the repaint cycle.
-->

---

# The Golden Rule of Swing
- All Swing component access must occur on the EDT
- Creation: new JFrame(), new JButton()
- Modification: setText(), setVisible(), add()
- Queries: getText(), isVisible(), getWidth()
- Violating this rule causes race conditions and UI corruption

<!--
This is the most important rule in Swing development. Write it on the board. Repeat it. Students must internalize this.
-->

---

# The Anti-Pattern: Main Thread Creation
- Creating Swing components directly in main() is WRONG
- main() executes on the Main Thread, NOT the EDT
- This violates the Golden Rule immediately
- May appear to work, but causes subtle race conditions
- Leads to unpredictable behavior and crashes

```java
// ANTI-PATTERN: Do NOT do this
public static void main(String[] args) {
    JFrame frame = new JFrame("Bad Example");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(400, 300);
    frame.setVisible(true); // WRONG THREAD!
}
```

<!--
Show students why this code is dangerous. It may work in simple cases but will fail in production with complex UIs or threading.
-->

---

# The Best Practice: SwingUtilities.invokeLater
- SwingUtilities.invokeLater() schedules a Runnable on the EDT
- Transfers execution from Main Thread to EDT safely
- All UI initialization code goes inside the Runnable
- This is the ONLY correct way to start a Swing app
- Use method references (::) for cleaner syntax

```java
// BEST PRACTICE: Always use invokeLater
public static void main(String[] args) {
    SwingUtilities.invokeLater(MyApp::createAndShowGUI);
}

private static void createAndShowGUI() {
    // All UI code here runs on the EDT
    JFrame frame = new JFrame("Correct Example");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(400, 300);
    frame.setVisible(true);
}
```

<!--
This is the foundation pattern. Every Swing app should start this way. Explain that invokeLater places the task in the event queue.
-->

---
layout: center
---

# Anti-Pattern vs Best Practice

![Anti-Pattern vs Best Practice](/images/03-antipattern-vs-bestpractice.jpg)

- Left: Main Thread creates UI - race conditions
- Right: EDT creates UI - thread-safe and correct
- Always use SwingUtilities.invokeLater() in main()
- Separate UI creation logic into dedicated methods

<!--
Visual comparison of the two approaches. Emphasize the safety and predictability of the right approach.
-->

---

# Code Walkthrough: The Robust Skeleton
- createAndShowGUI() - factory method for UI setup
- JFrame setup: title, close operation, content
- pack() - sizes window to preferred component sizes
- setLocationRelativeTo(null) - centers on screen
- setVisible(true) - final step, triggers EDT rendering

```java
public class SwingStarter {
    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Professional Swing App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel label = new JLabel("System Ready", SwingConstants.CENTER);
        frame.getContentPane().add(label);

        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SwingStarter::createAndShowGUI);
    }
}
```

<!--
This is the template for all professional Swing applications. Students should memorize this structure.
-->

---

# Container Types Overview
- JFrame - Main application window with title bar and borders
- JDialog - Modal or non-modal secondary windows
- JWindow - Bare window with no decorations (splash screens)
- All inherit from java.awt.Window
- Each serves different UI architectural needs

<!--
JFrame is the workhorse. JDialog for user prompts. JWindow for splash screens or tooltips. Explain modal vs non-modal dialogs.
-->

---
layout: center
---

# Container Hierarchy

![Container Hierarchy](/images/02-container-hierarchy.png)

- Window (root) -> Frame -> JFrame
- Window -> Dialog -> JDialog
- Window -> JWindow
- Inheritance hierarchy defines capabilities
- JFrame adds Swing-specific features to AWT Frame

<!--
Walk through the diagram. Show how Swing components (J-prefix) extend AWT components. This is a bridge between old and new.
-->

---

# Hands-On Exercise
- Task 1: Create a JFrame with a JButton using the Robust Skeleton
- Task 2: Add a JDialog that opens when the button is clicked
- Task 3: Make the dialog modal and display a message
- Task 4: Verify all operations occur on the EDT using System.out.println(SwingUtilities.isEventDispatchThread())
- Bonus: Add a JWindow splash screen before the main window

<!--
Give students 15 minutes. Walk around and help. Common mistakes: forgetting invokeLater, creating components in listeners without checking EDT.
-->

---

# Common Mistakes to Avoid
- Creating UI components in main() without invokeLater
- Blocking the EDT with long-running operations (network, file I/O)
- Accessing Swing components from background threads
- Forgetting to call pack() - leads to zero-size windows
- Calling setVisible(true) before adding components

<!--
These are the top 5 mistakes beginners make. Each one causes subtle bugs that are hard to debug. Emphasize EDT discipline.
-->

---

# Key Takeaways
- The EDT is the single thread for all Swing UI operations
- Always use SwingUtilities.invokeLater() to start Swing apps
- The Robust Skeleton pattern is your template for all projects
- JFrame for main windows, JDialog for secondary windows
- Thread discipline is non-negotiable in Swing development

<!--
Summarize the core principles. Reinforce that EDT mastery is the foundation for everything else in Swing.
-->

---
layout: end
---

# Next Steps
- Chapter 2: Layout Managers (BorderLayout, FlowLayout, GridBagLayout)
- Chapter 3: Event Handling and Listeners
- Chapter 4: Worker Threads and SwingWorker
- Practice: Build a multi-window calculator app
- Resources: Oracle Swing Tutorial, Effective Java (Item 78)

<!--
Preview upcoming topics. Assign the calculator exercise as homework. Provide links to official documentation.
-->
