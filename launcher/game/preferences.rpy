init python:
    if persistent.gl_enable is None:
        persistent.gl_enable = True
        
    config.gl_enable = persistent.gl_enable
    
    if persistent.windows_console is None:
        persistent.windows_console = False


screen preferences:
    
    frame:
        style_group "l"
        style "l_root"
        
        window:
    
            has vbox

            label _("Launcher Preferences")
            
            add HALF_SPACER

            
            hbox:

                frame:
                    style "l_indent"
                    xmaximum ONEHALF
                    xfill True
 
                    has vbox

                    # Projects directory selection.
                    add SEPARATOR2
                    
                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox
                        
                        text _("Projects Directory:")
            
                        add HALF_SPACER
            
                        
                        frame style "l_indent": 
                            if persistent.projects_directory:
                                textbutton _("[persistent.projects_directory!q]") action Jump("projects_directory_preference")
                            else:
                                textbutton _("Not Set") action Jump("projects_directory_preference")
                                
                        
                    add SPACER

                    # Text editor selection.
                    add SEPARATOR2
                    
                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox
                        
                        text _("Text Editor:")
            
                        add HALF_SPACER
                        
                        frame style "l_indent": 
                            if persistent.editor:
                                textbutton persistent.editor action Jump("editor_preference")
                            else:
                                textbutton _("Not Set") action Jump("editor_preference")
                        
                    add SPACER

                    # Update URL selection.
                    add SEPARATOR2

                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox
                        
                        text _("Update Channel:")
            
                        add HALF_SPACER
                        
                        frame style "l_indent": 
                            textbutton persistent.update_channel action Jump("update_preference")
                    
                frame:
                    style "l_indent"
                    xmaximum ONEHALF
                    xfill True
                    
                    has vbox
                    add SEPARATOR2
                    
                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox
                        
                        text _("Navigation Options:")
                    
                        add HALF_SPACER
                    
                        textbutton _("Include private names") style "l_checkbox" action ToggleField(persistent, "navigate_private")
                        textbutton _("Include library names") style "l_checkbox" action ToggleField(persistent, "navigate_library")

                    add SPACER
                    add SEPARATOR2
                    
                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox
                        
                        text _("Launcher Options:")
                    
                        add HALF_SPACER
                    
                        textbutton _("Hardware rendering") style "l_checkbox" action ToggleField(persistent, "gl_enable")
                        
                        if renpy.windows:
                            textbutton _("Console output") style "l_checkbox" action ToggleField(persistent, "windows_console")

                    add SPACER
                    add SEPARATOR2
                    
                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox
                        
                        text _("Actions:")
                    
                        add HALF_SPACER

                        textbutton _("Open launcher as project") style "l_nonbox" action [ project.Select("launcher"), Jump("front_page") ]


    textbutton _("Back") action Jump("front_page") style "l_left_button"

label projects_directory_preference:
    call choose_projects_directory
    jump preferences


label preferences:
    call screen preferences
    