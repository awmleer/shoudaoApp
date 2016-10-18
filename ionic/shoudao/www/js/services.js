angular.module('shoudao.services', [])

  .service('contacts',function ($rootScope) {
    var self=this;
    self.get_contacts= function () {
      var fields = ["displayName", "name", "phoneNumbers"];
      var options = new ContactFindOptions();
      options.filter = "";
      options.multiple = true;
      navigator.contacts.find(fields, self.get_contacts_success, self.get_contacts_error, options);
    };


    self.get_contacts_success= function (contacts) {

      // $rootScope.contacts=contacts;
      console.log(contacts);
      // $rootScope.contacts=JSON.stringify(contacts);//for DEBUG
      // var aResult = [];
      $rootScope.contacts={};
      for (var i = 0; i<contacts.length; i++) {
        console.log(contacts[i].phoneNumbers.length);
        if (contacts[i].phoneNumbers.length) {
          for (var j = 0;  j < contacts[i].phoneNumbers.length; j++) {
            console.log();
            $rootScope.contacts[contacts[i].phoneNumbers[j].value]={
              name:contacts[i].displayName,
              checked:false
            };
          }
        }
      }
      console.log($rootScope.contacts);
      $rootScope.$apply();
    };

    self.get_contacts_error= function () {
      alert("获取联系人失败");
    };

  })

  .filter("object_length",function () {
    return function (input) {
      // console.log(input);
      if (typeof (input) == undefined || input == null) {
        return '';
      }
      var array_tmp=Object.keys(input);
      return array_tmp.length;
    }
  })


  .factory('Chats', function() {
    // Might use a resource here that returns a JSON array

    // Some fake testing data
    var chats = [{
      id: 0,
      name: 'Ben Sparrow',
      lastText: 'You on your way?',
      face: 'img/ben.png'
    }, {
      id: 1,
      name: 'Max Lynx',
      lastText: 'Hey, it\'s me',
      face: 'img/max.png'
    }, {
      id: 2,
      name: 'Adam Bradleyson',
      lastText: 'I should buy a boat',
      face: 'img/adam.jpg'
    }, {
      id: 3,
      name: 'Perry Governor',
      lastText: 'Look at my mukluks!',
      face: 'img/perry.png'
    }, {
      id: 4,
      name: 'Mike Harrington',
      lastText: 'This is wicked good ice cream.',
      face: 'img/mike.png'
    }];

    return {
      all: function() {
        return chats;
      },
      remove: function(chat) {
        chats.splice(chats.indexOf(chat), 1);
      },
      get: function(chatId) {
        for (var i = 0; i < chats.length; i++) {
          if (chats[i].id === parseInt(chatId)) {
            return chats[i];
          }
        }
        return null;
      }
    };
  });



