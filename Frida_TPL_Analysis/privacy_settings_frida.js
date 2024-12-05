
function FBaccessContextGetter(FacebookSdk, context) {
    // For methods that require parameters, ensure you have valid ones to pass
    if(context != null) {
        try {
            var limitEventAndDataUsage = FacebookSdk.getLimitEventAndDataUsage(context);
            //console.log("[*] getLimitEventAndDataUsage explicitly called, returned: " + limitEventAndDataUsage);
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Method": "getLimitEventAndDataUsage", "Value": ' + limitEventAndDataUsage + '}');
            console.log('\n');
        } catch (e) {
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'getLimitEventAndDataUsage could not be called: ' + e.toString() + '"}');
            console.log('\n');
        }

    }
}

// This function periodically access Facebook getters
function FBaccessGetters(FacebookSdk) {
    try {
        var autoLogAppEventsEnabled = FacebookSdk.getAutoLogAppEventsEnabled();
        //console.log("[*] autoLogAppEventsEnabled explicitly called, returned: " + autoLogAppEventsEnabled);
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Method": "getAutoLogAppEventsEnabled", "Value": ' + autoLogAppEventsEnabled + '}');
        console.log('\n');
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'getAutoLogAppEventsEnabled could not be called: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        var autoInitEnabled = FacebookSdk.getAutoInitEnabled();
        //console.log("[*] getAutoInitEnabled explicitly called, returned: " + autoInitEnabled);
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Method": "getAutoInitEnabled", "Value": ' + autoInitEnabled + '}');
        console.log('\n');
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'getAutoInitEnabled could not be called: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        var advertiserIDCollectionEnabled = FacebookSdk.getAdvertiserIDCollectionEnabled();
        //console.log("[*] getAdvertiserIDCollectionEnabled explicitly called, returned: " + advertiserIDCollectionEnabled);
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Method": "getAdvertiserIDCollectionEnabled", "Value": ' + advertiserIDCollectionEnabled + '}');
        console.log('\n');
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'getAdvertiserIDCollectionEnabled could not be called: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        var codelessDebugLogEnabled = FacebookSdk.getCodelessDebugLogEnabled();
        //console.log("[*] getCodelessDebugLogEnabled explicitly called, returned: " + codelessDebugLogEnabled);
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Method": "getCodelessDebugLogEnabled", "Value": ' + codelessDebugLogEnabled + '}');
        console.log('\n');
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'getCodelessDebugLogEnabled could not be called: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        var codelessSetupEnabled = FacebookSdk.getCodelessSetupEnabled();
        //console.log("[*] getCodelessSetupEnabled explicitly called, returned: " + codelessSetupEnabled);
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Method": "getCodelessSetupEnabled", "Value": ' + codelessSetupEnabled + '}');
        console.log('\n');
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'getCodelessSetupEnabled could not be called: ' + e.toString() + '"}');
        console.log('\n');
    }
}

// Function to intercept Facebook setters
function interceptSetters(FacebookSdk) {
    try {
        // Original hook remains...
        FacebookSdk.setAdvertiserIDCollectionEnabled.implementation = function (paramBoolean) {
            var oldValue = FacebookSdk.getAdvertiserIDCollectionEnabled();
            //console.log("[*] setAdvertiserIDCollectionEnabled called with value: " + paramBoolean);
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Method": "setAdvertiserIDCollectionEnabled", "Enabled": true, "OldValue": ' + oldValue + ', "NewValue": ' + paramBoolean + '}');
            console.log('\n');
            this.setAdvertiserIDCollectionEnabled(paramBoolean);
        };
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'setAdvertiserIDCollectionEnabled could not be captured: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        // Hooking setCodelessDebugLogEnabled(boolean)
        FacebookSdk.setCodelessDebugLogEnabled.implementation = function (paramBoolean) {
            var oldValue = FacebookSdk.getCodelessDebugLogEnabled();
            //console.log("[*] setCodelessDebugLogEnabled called. Old Value: " + oldValue + ", New Value: " + paramBoolean);
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Method": "setCodelessDebugLogEnabled", "Enabled": true, "OldValue": ' + oldValue + ', "NewValue": ' + paramBoolean + '}');
            console.log('\n');
            this.setCodelessDebugLogEnabled(paramBoolean);
        };
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'setCodelessDebugLogEnabled could not be captured: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        // Hooking setLimitEventAndDataUsage(Context, boolean)
        FacebookSdk.setLimitEventAndDataUsage.implementation = function (context, paramBoolean) {
            var prefs = context.getSharedPreferences("com.facebook.sdk.appEventPreferences", 0);
            var oldValue = prefs.getBoolean("limitEventUsage", false);
            //console.log("[*] setLimitEventAndDataUsage called. Old Value: " + oldValue + ", New Value: " + paramBoolean);
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Method": "setLimitEventAndDataUsage", "Enabled": true, "OldValue": ' + oldValue + ', "NewValue": ' + paramBoolean + '}');
            console.log('\n');
            this.setLimitEventAndDataUsage(context, paramBoolean);
        };
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'setLimitEventAndDataUsage could not be captured: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        // Assuming setAutoInitEnabled(boolean) is in the FacebookSdk class or adjust accordingly
        FacebookSdk.setAutoInitEnabled.implementation = function (paramBoolean) {
            var oldValue = FacebookSdk.getAutoInitEnabled();
            //console.log("[*] setAutoInitEnabled called. Old Value: " + oldValue + ", New Value: " + paramBoolean);
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Method": "setAutoInitEnabled", "Enabled": true, "OldValue": ' + oldValue + ', "NewValue": ' + paramBoolean + '}');
            console.log('\n');
            this.setAutoInitEnabled(paramBoolean);
        };
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'setAutoInitEnabled could not be captured: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        // Assuming setAutoLogAppEventsEnabled(boolean) is in the FacebookSdk class or adjust accordingly
        FacebookSdk.setAutoLogAppEventsEnabled.implementation = function (paramBoolean) {
            var oldValue = FacebookSdk.getAutoLogAppEventsEnabled();
            //console.log("[*] setAutoLogAppEventsEnabled called. Old Value: " + oldValue + ", New Value: " + paramBoolean);
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Method": "setAutoLogAppEventsEnabled", "Enabled": true, "OldValue": ' + oldValue + ', "NewValue": ' + paramBoolean + '}');
            console.log('\n');
            this.setAutoLogAppEventsEnabled(paramBoolean);
        };
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'setAutoLogAppEventsEnabled could not be captured: ' + e.toString() + '"}');
        console.log('\n');
    }

    try {
        FacebookSdk.setAdvertiserIDCollectionEnabled.implementation = function (paramBoolean) {
            var oldValue = FacebookSdk.getAdvertiserIDCollectionEnabled();
            //console.log("[*] setAdvertiserIDCollectionEnabled called. Old Value: " + oldValue + ", New Value: " + paramBoolean);
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Method": "setAdvertiserIDCollectionEnabled", "Enabled": true, "OldValue": ' + oldValue + ', "NewValue": ' + paramBoolean + '}');
            console.log('\n');
            this.setAdvertiserIDCollectionEnabled(paramBoolean);
        };
    } catch (e) {
        console.log('\n');
        console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'setAdvertiserIDCollectionEnabled could not be captured: ' + e.toString() + '"}');
        console.log('\n');
    }
}

setTimeout(function() {
    Java.perform(function () {

        /*    ----------------------------    THIRD PARTY LIBRARIES    ----------------------------     */

        // TPL privacy settings identification
        // Attempt to use the Facebook SDK class

        // ------------------------- Facebook Core SDK -------------------------------------

        var FacebookSdk = null;
        try {
            FacebookSdk = Java.use('com.facebook.FacebookSdk');
            try {
                var version = FacebookSdk.getSdkVersion();
                console.log('\n');
                console.log('{"TPL": "Facebook SDK", "Type": "Core", "Integrated": true, "SDK_Version": "' + version + '"}');
                console.log('\n');
            } catch (e) {
                console.log('\n');
                console.log('{"TPL": "Facebook SDK", "Type": "Core", "Integrated": true, "SDK_Version": "Unknown", "Error": "Error retrieving Core version: ' + e.toString() + '"}');
                console.log('\n');
            }
            //console.log("[*] CORE Facebook SDK is integrated.");

        } catch (e) {
            //console.log("[*] CORE Facebook SDK is not integrated.");
            console.log('\n');
            console.log('{"TPL": "Facebook SDK", "Type": "Core", "Integrated": false}');
            console.log('\n');
        }

        // Function to check if the SDK is initialized and log getters
        function checkInitialization() {
            try {
                var FBsdkIsInitialized = FacebookSdk.isInitialized();
                console.log('\n');
                console.log('{"TPL": "Facebook SDK", "Type": "Core", "Initialized": ' + FBsdkIsInitialized + '}');
                console.log('\n');

                if (FBsdkIsInitialized) {
                    clearInterval(checkInitInterval); // Stop checking initialization
                    startLoggingGetters(); // Start logging getters every 5 seconds
                }
            } catch (e) {
                console.log('\n');
                console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "Failed to determine initialization status: ' + e.toString() + '"}');
                console.log('\n');
            }
        }

        // Function to continuously log getter values
        function logGetters() {
            FBaccessGetters(FacebookSdk);
            var context = null;
            try {
                context = FacebookSdk.getApplicationContext();
            } catch (e) {
                console.log('\n');
                console.log('{"TPL": "Facebook SDK", "Type": "Core", "Error": "' + 'Facebook Context could not be retrieved: ' + e.toString() + '"}');
                console.log('\n');
            }
            if (context != null) {
                FBaccessContextGetter(FacebookSdk, context);
            }
        }

        function startLoggingGetters() {
            logGetters(); // Log once immediately
            setInterval(logGetters, 5000); // Continue logging every 5 seconds
        }

        // If the Facebook Core SDK is integrated, then we call the getters and intercept the setters.
        if (FacebookSdk != null) {

            checkInitialization(); // Call immediately
            // Check initialization every second until initialized
            var checkInitInterval = setInterval(checkInitialization, 1000);

            // Hook setters irrespective of the initialization status
            interceptSetters(FacebookSdk);
        }

        // ------------------------- Facebook Audience Network SDK -------------------------------------

        try {
            Java.use('com.facebook.ads.AudienceNetworkActivity'); // Since 4.23
            try {
                var BuildConfig = Java.use('com.facebook.ads.BuildConfig');
                var versionName = BuildConfig.VERSION_NAME.value;
                console.log('\n')
                console.log(JSON.stringify({ "TPL": "Facebook SDK", "Type": "Audience Network", "Integrated": true, "SDK_Version": versionName }));
                console.log('\n')
            } catch (e) {
                console.log('\n')
                console.log('{"TPL": "Facebook SDK", "Type": "Audience Network", "Integrated": true, "SDK_Version": "Unknown", "Error": "Error retrieving Audience Network version: ' + e.toString() + '"}');
                console.log('\n')
            }
        } catch (e) {
            console.log('\n')
            console.log('{"TPL": "Facebook SDK", "Type": "Audience Network", "Integrated": false}');
            console.log('\n')
        }

        // Use the AdSettings class from the Facebook Ads SDK
        var AdInternalSettings;
        try {
            AdInternalSettings = Java.use('com.facebook.ads.internal.settings.AdInternalSettings');
        } catch (e) {

        }
        if (AdInternalSettings != null){
            try {
                //https://developers.facebook.com/docs/audience-network/optimization/best-practices/data-processing-options
                // Intercept the setDataProcessingOptions method
                AdInternalSettings.setDataProcessingOptions.overloads.forEach(function(overload) {
                    overload.implementation = function() {
                        var args = Array.prototype.slice.call(arguments);
                        if (args.length === 1) {
                            //console.log("[*] setDataProcessingOptions called with options: " + args[0]);
                            console.log('\n')
                            console.log('{"TPL": "Facebook SDK", "Type": "Audience Network", "Method": "setDataProcessingOptions", "Enabled": true, "DPO_Param1": ' + JSON.stringify(args[0]) + '}');
                            console.log('\n')
                        } else if (args.length === 3) {
                            //console.log("[*] setDataProcessingOptions called with options: " + args[0] + ", country: " + args[1] + ", state: " + args[2]);
                            console.log('\n')
                            console.log('{"TPL": "Facebook SDK", "Type": "Audience Network", "Method": "setDataProcessingOptions", "Enabled": true, "DPO_Param1": ' + JSON.stringify(args[0]) + ', "DPO_Param2": ' + JSON.stringify(args[1]) + ', "DPO_Param3": ' + JSON.stringify(args[2]) + '}');
                            console.log('\n')
                        }
                        this.setDataProcessingOptions.apply(this, arguments);
                    };
                });
            } catch (e) {
                //console.log("[Facebook SDK error]: " + e);
                console.log('\n')
                console.log('{"TPL": "Facebook SDK", "Type": "Audience Network", "Error": "setDataProcessingOptions could not be intercepted: ' + e.toString() + '"}');
                console.log('\n')
            }
        }

        // Use the AdSettings class from the Facebook Ads SDK
        var AdSettings;
        try {
            AdSettings = Java.use('com.facebook.ads.AdSettings');
        } catch (e) {

        }
        if (AdSettings != null) {
            try {
                //COPPA Recommendation: https://developers.facebook.com/docs/audience-network/optimization/best-practices/coppa
                //https://developers.facebook.com/docs/audience-network/reference/android/com/facebook/ads/adsettings.html/?version=v6.8.0
                // Mixed Audience setting should be enabled when you are targeting children among others.
                AdSettings.setMixedAudience.implementation = function (paramBoolean) {
                    //console.log("[*] setting mixedAudience parameter to: " + paramBoolean);
                    console.log('\n')
                    console.log('{"TPL": "Facebook SDK", "Type": "Audience Network", "Method": "setMixedAudience", "Enabled": true, "OldValue": ' + 'Unknown' + ', "NewValue": ' + paramBoolean + '}');
                    console.log('\n')
                    this.setMixedAudience(paramBoolean);
                };
            } catch (e) {
                //console.log("[Error setting Facebook Mixed Audience]: " + e)
                console.log('\n')
                console.log('{"TPL": "Facebook SDK", "Type": "Audience Network", "Error": "setMixedAudience could not be intercepted: ' + e.toString() + '"}');
                console.log('\n')
            }
        }
    });
}, 0);