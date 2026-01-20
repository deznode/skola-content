package dev.skola.events;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * Java Swing Events Tutorial - Complete Solution
 * Demonstrates various event handling patterns in Swing.
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

        // Window events
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                log("Window closing...");
            }

            @Override
            public void windowOpened(WindowEvent e) {
                log("Window opened!");
            }
        });

        // Key events on the frame
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                log("Key pressed: " + KeyEvent.getKeyText(e.getKeyCode()));
            }
        });

        setFocusable(true);
        pack();
        setLocationRelativeTo(null);
    }

    private JPanel createButtonPanel() {
        JPanel panel = new JPanel(new FlowLayout());

        // Button with ActionListener (lambda)
        JButton clickButton = new JButton("Click Me");
        clickButton.addActionListener(e -> {
            clickCount++;
            statusLabel.setText("Clicks: " + clickCount);
            log("Button clicked! Count: " + clickCount);
        });

        // Button with anonymous class
        JButton resetButton = new JButton("Reset");
        resetButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                clickCount = 0;
                statusLabel.setText("Reset!");
                log("Counter reset");
            }
        });

        // Toggle button
        JToggleButton toggleButton = new JToggleButton("Toggle");
        toggleButton.addItemListener(e -> {
            boolean selected = e.getStateChange() == ItemEvent.SELECTED;
            log("Toggle: " + (selected ? "ON" : "OFF"));
        });

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

        // Mouse listener for clicks
        panel.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                String button = switch (e.getButton()) {
                    case MouseEvent.BUTTON1 -> "Left";
                    case MouseEvent.BUTTON2 -> "Middle";
                    case MouseEvent.BUTTON3 -> "Right";
                    default -> "Unknown";
                };
                log(String.format("Mouse clicked: %s at (%d, %d)", button, e.getX(), e.getY()));
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                statusLabel.setText("Mouse entered panel");
            }

            @Override
            public void mouseExited(MouseEvent e) {
                statusLabel.setText("Mouse left panel");
            }
        });

        // Mouse motion listener
        panel.addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseMoved(MouseEvent e) {
                statusLabel.setText(String.format("Position: (%d, %d)", e.getX(), e.getY()));
            }

            @Override
            public void mouseDragged(MouseEvent e) {
                statusLabel.setText(String.format("Dragging: (%d, %d)", e.getX(), e.getY()));
            }
        });

        return panel;
    }

    private JPanel createBottomPanel() {
        JPanel panel = new JPanel(new FlowLayout());

        // Text field with key listener
        JTextField textField = new JTextField(15);
        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                log("Text: " + textField.getText());
            }
        });

        // Combo box with item listener
        JComboBox<String> comboBox = new JComboBox<>(new String[]{"Option 1", "Option 2", "Option 3"});
        comboBox.addItemListener(e -> {
            if (e.getStateChange() == ItemEvent.SELECTED) {
                log("Selected: " + e.getItem());
            }
        });

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
