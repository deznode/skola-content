package dev.skola.events;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * Java Swing Events Tutorial - Starter Code
 * Complete the TODOs to learn event handling in Swing.
 */
public class EventDemo extends JFrame {
    private final JLabel statusLabel;
    private final JTextArea logArea;
    private int clickCount = 0;

    public EventDemo() {
        setTitle("Swing Events Demo");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));

        // Top panel with buttons
        JPanel buttonPanel = createButtonPanel();
        add(buttonPanel, BorderLayout.NORTH);

        // Center panel with mouse tracking area
        JPanel mousePanel = createMousePanel();
        add(mousePanel, BorderLayout.CENTER);

        // Bottom panel with status and log
        JPanel bottomPanel = createBottomPanel();
        add(bottomPanel, BorderLayout.SOUTH);

        // Status label
        statusLabel = new JLabel("Ready");
        add(statusLabel, BorderLayout.WEST);

        // Log area
        logArea = new JTextArea(5, 30);
        logArea.setEditable(false);
        add(new JScrollPane(logArea), BorderLayout.EAST);

        // TODO: Add a WindowListener to handle window events
        // Use WindowAdapter and override:
        // - windowClosing: log "Window closing..."
        // - windowOpened: log "Window opened!"

        // TODO: Add a KeyListener to handle keyboard events
        // Use KeyAdapter and override keyPressed to log the key

        setFocusable(true);
        pack();
        setLocationRelativeTo(null);
    }

    private JPanel createButtonPanel() {
        JPanel panel = new JPanel(new FlowLayout());

        // Button with ActionListener
        JButton clickButton = new JButton("Click Me");
        // TODO: Add an ActionListener using a lambda expression
        // When clicked:
        // 1. Increment clickCount
        // 2. Update statusLabel with "Clicks: " + clickCount
        // 3. Log "Button clicked! Count: " + clickCount

        // Button with anonymous class
        JButton resetButton = new JButton("Reset");
        // TODO: Add an ActionListener using an anonymous class
        // When clicked:
        // 1. Reset clickCount to 0
        // 2. Update statusLabel with "Reset!"
        // 3. Log "Counter reset"

        // Toggle button
        JToggleButton toggleButton = new JToggleButton("Toggle");
        // TODO: Add an ItemListener to handle toggle state changes
        // Check if e.getStateChange() == ItemEvent.SELECTED
        // Log "Toggle: ON" or "Toggle: OFF" accordingly

        panel.add(clickButton);
        panel.add(resetButton);
        panel.add(toggleButton);
        return panel;
    }

    private JPanel createMousePanel() {
        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.LIGHT_GRAY);
                g.drawString("Move mouse here", 10, 20);
            }
        };
        panel.setPreferredSize(new Dimension(300, 150));
        panel.setBorder(BorderFactory.createTitledBorder("Mouse Tracking Area"));

        // TODO: Add a MouseListener using MouseAdapter
        // Override:
        // - mouseClicked: log the button (Left/Middle/Right) and coordinates
        //   Hint: Use e.getButton() and compare with MouseEvent.BUTTON1, etc.
        // - mouseEntered: update statusLabel with "Mouse entered panel"
        // - mouseExited: update statusLabel with "Mouse left panel"

        // TODO: Add a MouseMotionListener using MouseMotionAdapter
        // Override:
        // - mouseMoved: update statusLabel with current position
        // - mouseDragged: update statusLabel with "Dragging: (x, y)"

        return panel;
    }

    private JPanel createBottomPanel() {
        JPanel panel = new JPanel(new FlowLayout());

        // Text field with key listener
        JTextField textField = new JTextField(15);
        // TODO: Add a KeyListener using KeyAdapter
        // Override keyReleased to log the current text content

        // Combo box with item listener
        JComboBox<String> comboBox = new JComboBox<>(new String[]{"Option 1", "Option 2", "Option 3"});
        // TODO: Add an ItemListener to handle selection changes
        // Only log when e.getStateChange() == ItemEvent.SELECTED
        // Log "Selected: " + the selected item

        panel.add(new JLabel("Type:"));
        panel.add(textField);
        panel.add(new JLabel("Select:"));
        panel.add(comboBox);
        return panel;
    }

    private void log(String message) {
        logArea.append(message + "\n");
        logArea.setCaretPosition(logArea.getDocument().getLength());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new EventDemo().setVisible(true);
        });
    }
}
